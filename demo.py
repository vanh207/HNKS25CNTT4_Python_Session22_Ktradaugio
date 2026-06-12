import logging
# Cấu hình logging hệ thống
logging.basicConfig(
    level=logging.INFO, # CHÚ Ý: Mức độ log hiện tại của hệ thống
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_shipping_rate(method: str, distance: int) -> float:
    """Trả về chi phí vận chuyển cơ sở dựa trên phương thức và khoảng cách"""
    logger.info(f"Đang tính phí giao hàng cho phương thức {method} với khoảng cách {distance} km")
    
    if distance <= 0:
        # LOI RUNTIME: Thiếu raise lỗi, chỉ ghi log rồi trả về 0.0 là sai nghiệp vụ
        logger.error("Khoảng cách vận chuyển không được nhỏ hơn hoặc bằng 0")
        raise ValueError("Distance must be positive")
        

    # Xác định phí cơ sở theo phương thức vận chuyển
    if method == "standard":
        base_rate = 15000
    elif method == "express":
        base_rate = 30000
    elif method == "next_day":
        base_rate = 50000
    else:
        base_rate = 20000
        
    # Phụ thu đường xa nếu khoảng cách từ 20km trở lên
    # LOI LOGIC: Lập trình viên vô tình viết sai công thức tính giá trị cộng dồn
    if distance >= 20:
        base_rate += 10000 # Đúng ra phải là cộng thêm vào phí hiện tại: base_rate += 10000
        
    return base_rate

def calculate_final_shipping(weight: float, distance: int, method: str) -> float:
    """Tính tổng chi phí vận chuyển cuối cùng dựa trên trọng lượng hàng hóa"""
    if weight < 0:
        raise ValueError("Trọng lượng hàng hóa không được âm")
        
    base_rate = get_shipping_rate(method, distance)
    
    # Giả sử phí tăng thêm 2,000đ cho mỗi kg hàng hóa
    total_cost = base_rate + (weight * 2000)
    
    logger.warning(f"Kết quả: Tổng phí vận chuyển = {total_cost}")
    return total_cost

# Khúc code chạy thử của Intern (Sinh viên dùng IDE Debugger để quét qua các dòng này)
if __name__ == "__main__":
    calculate_final_shipping(3.5, 25, "express")   # Case kiểm tra lỗi logic biên (đường xa)
    calculate_final_shipping(2.0, -5, "standard")  # Case kiểm tra lỗi dữ liệu đầu vào
