# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Phi Nhật  
> **Mã Sinh Viên / Mã Học viên:** 2A202602658  
> **Chủ đề Lựa chọn:** Gợi ý 4.3: Trợ lý Tư vấn Sức khỏe Vinmec: Tra cứu lịch làm việc bác sĩ chuyên khoa và đặt lịch khám bệnh.

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 5 / 5 | Bài toán yêu cầu suy luận đa bước rõ ràng: Tra cứu lịch làm việc của bác sĩ chuyên khoa phù hợp trước, sau đó mới đặt lịch khám. |
| **2. Tool Interaction** | 5 / 5 | Agent cần kết nối với MCP Server để gọi các tool tìm bác sĩ (doctor_schedule_query) và đặt lịch (book_health_check). |
| **3. Dynamic Decision** | 4 / 5 | Agent phải ra quyết định dựa trên lịch rảnh của bác sĩ để đề xuất giờ phù hợp hoặc thông báo không có lịch. |
| **4. Long Horizon Goal** | 4 / 5 | Quá trình từ tra cứu đến đặt lịch phải duy trì thông tin bệnh nhân và chuyên khoa bác sĩ. |
| **TỔNG ĐIỂM AGENTIC FIT** | **18 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu lịch làm việc của bác sĩ chuyên khoa Tim Mạch.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "doctor_schedule_query",
    "arguments": {
      "specialty": "Tim Mạch"
    },
    "observation": {
      "status": "SUCCESS",
      "specialty": "Tim Mạch",
      "data": {
        "doctor_name": "PGS.TS Phạm Văn Tim",
        "available_slots": [
          "09:00",
          "14:00"
        ],
        "room": "Phòng 101"
      }
    },
    "latency_ms": 0.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
