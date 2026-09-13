"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu lịch bác sĩ
    {
        "name": "doctor_schedule_query",
        "description": "Tra cứu lịch làm việc của bác sĩ theo chuyên khoa tại Vinmec.",
        "parameters": {
            "type": "object",
            "properties": {
                "specialty": {
                    "type": "string",
                    "description": "Tên chuyên khoa cần tra cứu (ví dụ: 'Tim Mạch', 'Tiêu Hóa')"
                }
            },
            "required": ["specialty"]
        }
    },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HOÀN THIỆN TOOL SCHEMA CHO 'book_health_check'
    # --------------------------------------------------------------------------
    {
        "name": "book_health_check",
        "description": "Đặt lịch khám bệnh tại Vinmec.",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_id": {
                    "type": "string",
                    "description": "Mã bệnh nhân (ví dụ: 'BN123456')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn khám (ví dụ: '09:00 20/09/2026')"
                },
                "doctor_name": {
                    "type": "string",
                    "description": "Tên bác sĩ chuyên khoa"
                }
            },
            "required": ["patient_id", "datetime_str", "doctor_name"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_PATIENT_DB = {
    "BN123456": {
        "full_name": "Nguyễn Văn Bệnh",
        "age": 45,
        "history": "Huyết áp cao"
    }
}

MOCK_DOCTOR_DB = {
    "Tim Mạch": {
        "doctor_name": "PGS.TS Phạm Văn Tim",
        "available_slots": ["09:00", "14:00"],
        "room": "Phòng 101"
    },
    "Tiêu Hóa": {
        "doctor_name": "TS.BS Lê Thị Ruột",
        "available_slots": ["10:00", "15:00"],
        "room": "Phòng 205"
    }
}


def execute_doctor_schedule_query(specialty: str) -> str:
    """Thực thi tra cứu lịch bác sĩ theo chuyên khoa"""
    doctor = MOCK_DOCTOR_DB.get(specialty)
    if doctor:
        return json.dumps({
            "status": "SUCCESS",
            "specialty": specialty,
            "data": doctor
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy bác sĩ cho chuyên khoa '{specialty}'"
        }, ensure_ascii=False)


def execute_book_health_check(patient_id: str, datetime_str: str, doctor_name: str) -> str:
    """Thực thi đặt lịch khám bệnh"""
    # Mô phỏng kiểm tra bệnh nhân
    if patient_id not in MOCK_PATIENT_DB:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy hồ sơ bệnh nhân có mã '{patient_id}'. Vui lòng kiểm tra lại."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{patient_id}-99",
        "patient_id": patient_id,
        "datetime": datetime_str,
        "doctor": doctor_name,
        "message": f"Đặt lịch khám thành công cho bệnh nhân {patient_id} với bác sĩ {doctor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "doctor_schedule_query": execute_doctor_schedule_query,
    "book_health_check": execute_book_health_check
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)

if __name__ == "__main__":
    print(f"✅ [TOOLS CHECK]: Đã đăng ký thành công {len(TOOLS_SCHEMA)} Native Tools trong TOOLS_SCHEMA!")
    print("🧪 Kết quả gọi thử doctor_schedule_query:")
    test_result = dispatch_tool_call("doctor_schedule_query", {"specialty": "Tim Mạch"})
    print(test_result)
