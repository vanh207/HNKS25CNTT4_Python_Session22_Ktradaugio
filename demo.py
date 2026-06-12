import logging

# Cấu hình logging hệ thống
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_shipping_rate(method: str, distance: int) -> float:
    """Trả về chi phí vận chuyển cơ sở dựa trên phương thức và khoảng cách"""
    logger.info(f"Đang tính phí giao hàng cho phương thức {method} với khoảng cách {distance} km")
    
    # 1. SỬA LỖI RUNTIME: Ném ra ngoại lệ (raise) để chặn đứng dữ liệu sai, không cho chạy tiếp
    if distance <= 0:
        logger.error(f"Khoảng cách vận chuyển không hợp lệ: {distance} km")
        raise ValueError("Khoảng cách vận chuyển phải lớn hơn 0")
        
    # Xác định phí cơ sở theo phương thức vận chuyển
    if method == "standard":
        base_rate = 15000
    elif method == "express":
        base_rate = 30000
    elif method == "next_day":
        base_rate = 50000
    else:
        base_rate = 20000
        
    # 2. SỬA LỖI LOGIC: Sử dụng toán tử += để cộng dồn 10,000đ vào phí cơ sở ban đầu
    if distance >= 20:
        base_rate += 10000  # Viết tường minh: base_rate = base_rate + 10000
        
    return base_rate

def calculate_final_shipping(weight: float, distance: int, method: str) -> float:
    """Tính tổng chi phí vận chuyển cuối cùng dựa trên trọng lượng hàng hóa"""
    if weight < 0:
        logger.error(f"Trọng lượng hàng hóa không hợp lệ: {weight} kg")
        raise ValueError("Trọng lượng hàng hóa không được âm")
    try:
        base_rate = get_shipping_rate(method, distance)
        total_cost = base_rate + (weight * 2000)
        logger.warning(f"Kết quả: Tổng phí vận chuyển = {total_cost} đ")
        return total_cost
    except ValueError as e:
        logger.error(f"Xử lý thất bại do lỗi dữ liệu: {e}")
        return 0.0 # Hoặc xử lý theo nghiệp vụ (ví dụ: yêu cầu khách nhập lại)

# Khúc code chạy thử
if __name__ == "__main__":
    calculate_final_shipping(3.5, 25, "express")   
    calculate_final_shipping(2.0, -5, "standard")