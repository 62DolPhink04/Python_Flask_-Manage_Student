import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Khởi tạo Flask và cấu hình SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = '2014'

# Xác định đường dẫn tuyệt đối đến tệp cơ sở dữ liệu
database_file = os.path.join(app.root_path, 'du_lieu', 'ql_truong_hoc.db')
app.config['DATABASE_FILE'] = database_file

# Cấu hình SQLAlchemy URI với check_same_thread=False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.config["DATABASE_FILE"]}?check_same_thread=False'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

# Import các module khác
from app_school.xu_ly.Xu_ly_Model import Base, db_session
import app_school.app_gateway
import app_school.app_giao_vien
import app_school.app_lop_hoc
import app_school.app_hoc_sinh
import app_school.app_trang_chu
import app_school.app_thoi_khoa_bieu
import app_school.app_lich_thi
import app_school.app_quan_li
import app_school.app_hoat_dong
