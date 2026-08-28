from pathlib import Path
import pandas as pd   
from datetime import datetime 
from langchain_core.tools import tool


@tool
def w_pd(date: datetime, content: str) -> str:
    """
    Thêm nội dung vào lịch trình cá nhân tại một ngày cụ thể.

    Tool này dùng để GHI hoặc CẬP NHẬT lịch trình cá nhân trong schedule.csv.

    Args:
        date:
            Ngày cần ghi lịch trình.
            Chỉ dùng ngày/thời gian mà người dùng đã cung cấp hoặc đã được
            xác định rõ từ ngữ cảnh. Không tự ý tạo ngày nếu chưa đủ thông tin.

        content:
            Nội dung lịch trình cần thêm vào ngày đó.
            Nội dung mới sẽ được nối thêm vào nội dung đã có của ngày,
            không ghi đè nội dung cũ.

    Returns:
        Thông báo xác nhận việc ghi lịch thành công.

    Notes:
        - Nếu ngày chưa tồn tại trong lịch, một mục mới sẽ được tạo.
        - Nếu ngày đã tồn tại, nội dung mới được thêm vào nội dung hiện có.
        - Tool này dùng cho dữ liệu lịch trình cá nhân, không phải để lưu
          kiến thức chung hoặc memory của model.
    """

    schedule_path = Path(__file__).parent.parent.parent.parent.parent.resolve()/"data"/"schedule.csv"
    schedule= pd.read_csv(schedule_path, index_col = 'date') 
    schedule.index = pd.to_datetime(schedule.index).tz_localize(None)
    date= pd.Timestamp(date).tz_localize(None)
    if date not in schedule.index:
        schedule.loc[date, "content"] = ""

    schedule.loc[date, "content"] += content +"\n"
    schedule= schedule.sort_index()
    schedule.to_csv(schedule_path)
    return "Đã viết lịch trình thành công."


@tool
def read_pd(datetime_from: datetime, datetime_to: datetime) -> dict:
    """
    Đọc lịch trình cá nhân trong một khoảng thời gian.

    Tool này dùng để TRA CỨU các sự kiện, công việc hoặc nội dung lịch trình
    đã được lưu trong schedule.csv.

    Args:
        datetime_from:
            Thời điểm bắt đầu của khoảng thời gian cần đọc.

        datetime_to:
            Thời điểm kết thúc của khoảng thời gian cần đọc.

    Returns:
        Dictionary có dạng:
        {
            datetime: "nội dung lịch trình"
        }

        Mỗi key là một ngày/thời điểm trong khoảng được yêu cầu,
        value là nội dung lịch trình tương ứng.

    Notes:
        - Chỉ đọc dữ liệu đã có trong lịch trình.
        - Không tự tạo hoặc suy diễn sự kiện chưa được lưu.
        - Dùng tool này khi cần kiểm tra lịch, tìm sự kiện,
          hoặc lấy thông tin lịch trình để lập kế hoạch.
        - Nếu người dùng hỏi về lịch trong một khoảng thời gian,
          hãy truyền đúng khoảng thời gian đó thay vì đọc toàn bộ lịch.
    """
    schedule_path = Path(__file__).parent.parent.parent.parent.parent.resolve()/"data"/"schedule.csv"
    schedule= pd.read_csv(schedule_path, index_col= 'date') 
    schedule.index = pd.to_datetime(schedule.index).tz_localize(None)
    schedule= schedule.sort_index()
    datetime_from = pd.Timestamp(datetime_from).tz_localize(None)
    datetime_to   = pd.Timestamp(datetime_to).tz_localize(None)
    content = schedule.loc[datetime_from:datetime_to]
    if content.empty:
        return {
            "status": "success",
            "message": "Không có lịch trình nào trong khoảng thời gian này.",
            "data": {}
        }


    content_dict = {}

    for date in content.index:
        content_dict[date] = content.loc[date, "content"]

    return {
        "status": "success",
        "data": content_dict
    }
tools= [w_pd, read_pd]