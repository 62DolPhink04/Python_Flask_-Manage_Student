from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SubmitField, SelectField, PasswordField
from wtforms import validators

class Form_Register(FlaskForm):
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])
    Th_Taikhoan = StringField("Tên tài khoản đăng nhập", [
        validators.DataRequired("Vui lòng nhập vào tên đăng nhập"),
        validators.Length(min=4, max=20)
    ])
    Th_Matkhau = PasswordField("Mật khẩu", [
        validators.DataRequired(),
        validators.Length(min=4, max=20),
        validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu xác nhận phải trùng nhau')
    ])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")

class Form_Login(FlaskForm):
    Th_Vaitro = SelectField("Vai trò", choices=[('gv', 'Giáo Viên'), ('hs', 'Học Sinh'), ('ql', 'Quản Lý')])
    Th_Taikhoan = StringField("Tên tài khoản đăng nhập", [
        validators.DataRequired("Vui lòng nhập vào tên đăng nhập"),
        validators.Length(min=1, max=20)
    ])
    Th_Matkhau = PasswordField("Mật khẩu", [
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])

class RecoverPasswordForm(FlaskForm):
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])

class Form_Feedback(FlaskForm):
    Th_Ho_ten = StringField("Họ và tên", [
        validators.DataRequired("Vui lòng nhập họ tên."),
        validators.Length(min=4, max=30)
    ])
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])
    Th_Feedback = TextAreaField("Feedback", [
        validators.DataRequired("Vui lòng nhập phản hồi.")
    ])

class Form_Update_Gv(FlaskForm):
    Th_Ho_ten = StringField("Họ và tên", [
        validators.DataRequired("Vui lòng nhập họ tên."),
        validators.Length(min=4, max=30)
    ])
    Th_Gioi_tinh = SelectField("Giới tính", choices=[("Nam", "Nam"), ("Nữ", "Nữ"), ("Khác", "Khác")])
    Th_Ngay_sinh = StringField("Ngày sinh", [
        validators.DataRequired("Vui lòng nhập ngày sinh.")
    ])
    Th_Dia_chi = StringField("Địa chỉ", [
        validators.DataRequired("Vui lòng nhập vào địa chỉ"),
        validators.Length(min=4, max=75)
    ])
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])
    Th_Sdt = StringField("Số điện thoại", [
        validators.DataRequired("Vui lòng nhập vào số điện thoại"),
        validators.Length(min=4, max=15)
    ])
    Th_Trinh_do = StringField("Trình độ", [
        validators.DataRequired("Vui lòng nhập vào trình độ")
    ])
    Th_Chuyen_mon = StringField("Chuyên môn")

class Form_Update_Hs(FlaskForm):
    Th_Ho_ten = StringField("Họ và tên", [
        validators.DataRequired("Vui lòng nhập họ tên."),
        validators.Length(min=4, max=30)
    ])
    Th_Mat_khau = StringField("Mật Khẩu (tùy chọn)")
    Th_Gioi_tinh = SelectField("Giới tính", choices=[("Nam", "Nam"), ("Nữ", "Nữ"), ("Khác", "Khác")])
    Th_Ngay_sinh = StringField("Ngày sinh", [
        validators.DataRequired("Vui lòng nhập ngày sinh.")
    ])
    Th_Sdt = StringField("Số điện thoại", [
        validators.DataRequired("Vui lòng nhập vào số điện thoại"),
        validators.Length(min=4, max=15)
    ])
    Th_Sdt_PH = StringField("Số điện thoại phụ huynh", [
        validators.DataRequired("Vui lòng nhập vào số điện thoại phụ huynh"),
        validators.Length(min=4, max=15)
    ])
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])
    Th_Dia_chi = StringField("Địa chỉ", [
        validators.DataRequired("Vui lòng nhập vào địa chỉ"),
        validators.Length(min=4, max=75)
    ])

class Form_Update_Ql(FlaskForm):
    Th_Ho_ten = StringField("Họ và tên", [
        validators.DataRequired("Vui lòng nhập họ tên."),
        validators.Length(min=4, max=30)
    ])
    Th_Mat_khau = StringField("Mật Khẩu (tùy chọn)")
    Th_Gioi_tinh = SelectField("Giới tính", choices=[("Nam", "Nam"), ("Nữ", "Nữ"), ("Khác", "Khác")])
    Th_Ngay_sinh = StringField("Ngày sinh", [
        validators.DataRequired("Vui lòng nhập ngày sinh.")
    ])
    Th_Sdt = StringField("Số điện thoại", [
        validators.DataRequired("Vui lòng nhập vào số điện thoại"),
        validators.Length(min=4, max=15)
    ])
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])
    Th_Dia_chi = StringField("Địa chỉ", [
        validators.DataRequired("Vui lòng nhập vào địa chỉ"),
        validators.Length(min=4, max=75)
    ])

class Form_Update_Manager(FlaskForm):
    Th_Ho_ten = StringField("Họ và tên", [
        validators.DataRequired("Vui lòng nhập họ tên."),
        validators.Length(min=4, max=30)
    ])
    Th_Gioi_tinh = SelectField("Giới tính", choices=[("M", "Nam"), ("F", "Nữ"), ("D", "Khác")])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Email = StringField("Email", [
        validators.DataRequired("Vui lòng nhập vào Email"),
        validators.Email("Vui lòng nhập vào Email"),
        validators.Length(min=4, max=30)
    ])
    Th_Tuoi = StringField("Tuổi", [
        validators.DataRequired("Vui lòng nhập vào tuổi"),
        validators.Length(min=1, max=3)
    ])
    Th_Sdt = StringField("Số điện thoại", [
        validators.DataRequired("Vui lòng nhập vào số điện thoại"),
        validators.Length(min=4, max=15)
    ])
    Th_Matkhau = PasswordField("Mật khẩu", [
        validators.DataRequired(),
        validators.Length(min=4, max=20),
        validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu xác nhận phải trùng nhau')
    ])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")

class Form_Create_Class(FlaskForm):
    Th_Lop = StringField("Tên Lớp", [
        validators.DataRequired("Vui lòng nhập tên lớp."),
        validators.Length(min=2, max=30)
    ])
    Th_Dia_diem = StringField("Địa điểm", [
        validators.DataRequired("Vui lòng nhập địa điểm."),
        validators.Length(min=5, max=75)
    ])
    Th_Khoi = SelectField("Khối", coerce=int)
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_GV_Chu_nhiem = SelectField("GV Chủ nhiệm", coerce=int)

class Form_Them_Nien_khoa(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa")

class Form_Chon_TKB(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_Lop = SelectField("Lớp", coerce=int)

class Form_Cap_nhat_TKB(FlaskForm):
    Th_Nien_khoa = StringField("Niên Khóa")
    Th_Lop = StringField("Lớp")
    Th_Thu = StringField("Thứ")
    Th_Tiet = StringField("Tiết")

    Th_Giao_vien = SelectField("Giáo viên", coerce=int)
    Th_Mon = SelectField("Môn", coerce=int)

class Form_Reset_pw(FlaskForm):
    Th_MatkhauCu = PasswordField("Mật khẩu cũ: ", [
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])
    Th_MatkhauMoi = PasswordField("Mật khẩu mới: ", [
        validators.DataRequired(),
        validators.Length(min=4, max=20),
        validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu xác nhận phải trùng nhau')
    ])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận: ")

class Form_Diem(FlaskForm):
    Th_Ho_ten = StringField("Họ và tên", [
        validators.DataRequired("Vui lòng nhập họ tên."),
        validators.Length(min=4, max=30)
    ])
    Th_Hoc_Ky = SelectField("Học Kỳ", choices=[('1', 'Học Kỳ 1'), ('2', 'Học Kỳ 2')])
    Th_Mon_hoc = SelectField("Môn học", coerce=int)
    Th_Diem = FloatField("Điểm", [
        validators.DataRequired("Vui lòng nhập điểm.")
    ])
    Th_Thu = StringField("Thứ")
    Th_Buoi = StringField("Buổi")
    Th_Tiet = StringField("Tiết")

class Form_Lich_Thi(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_Khoi = SelectField("Khối", coerce=int)

class Form_Them_Lich_Thi(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)
    Th_Khoi = SelectField("Khối", coerce=int)
    Th_Mon = SelectField("Môn", coerce=int)
    Th_NgayThi = StringField("Ngày thi", [
        validators.DataRequired("Vui lòng nhập ngày thi.")
    ])
    Th_ThoiGian = StringField("Thời Gian", [
        validators.DataRequired()
    ])

class Form_Sua_Lich_Thi(FlaskForm):
    Th_NgayThi = StringField("Ngày thi", [
        validators.DataRequired("Vui lòng nhập ngày thi.")
    ])
    Th_ThoiGian = StringField("Thời Gian", [
        validators.DataRequired()
    ])

class Form_Xem_Hoat_Dong(FlaskForm):
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)

class Form_Them_Hoat_Dong(FlaskForm):
    Th_TieuDe = StringField("Tiêu đề", [
        validators.DataRequired("Vui lòng nhập tiêu đề.")
    ])
    Th_NoiDung = TextAreaField("Nội dung", [
        validators.DataRequired(), 
        validators.Length(min=4, max=500)
    ])
    Th_HanDangKy = StringField("Hạn đăng ký", [
        validators.DataRequired("Vui lòng nhập hạn đăng ký.")
    ])
    Th_Nien_khoa = SelectField("Niên Khóa", coerce=int)

class Form_Sua_Hoat_Dong(FlaskForm):
    Th_TieuDe = StringField("Tiêu đề", [
        validators.DataRequired("Vui lòng nhập tiêu đề.")
    ])
    Th_NoiDung = TextAreaField("Nội dung", [
        validators.DataRequired(), 
        validators.Length(min=4, max=500)
    ])
    Th_HanDangKy = StringField("Hạn đăng ký", [
        validators.DataRequired("Vui lòng nhập hạn đăng ký.")
    ])
    Th_Nien_khoa = SelectField("Niên khóa", coerce=int)

'''class Form_UpdateProfile(FlaskForm) :
    Th_Id = IntegerField("Mã số ID" , [validators.Required("Vui lòng nhập vào mã số ID") ,validators.Length(min=4, max=15)])
    Th_Taikhoan = TextField("Tên tài khoản đăng nhập" , [validators.Required("Vui lòng nhập vào tên đăng nhập"),validators.Length(min=4, max=20)])
    Th_Matkhau = PasswordField("Mật khẩu" , [validators.InputRequired() ,validators.Length(min=4, max=20), validators.EqualTo('Th_Mat_khau_xac_nhan', message='Mật khẩu và mật khẩu đăng nhập phải trùng nhau')])
    Th_Mat_khau_xac_nhan = PasswordField("Mật khẩu xác nhận")
    Th_quyen = RadioField("Chức vụ" , choices=[ ("T", "Giáo viên") , ("H" , "Học sinh") , ("Q" , "Quản lý") ])
    Th_Ho_ten = TextField("Họ và tên" ,[validators.Required("Vui lòng nhập họ tên.") ,validators.Length(min=4, max=30)])
    Th_Lop = IntegerField("Lớp" , [validators.Required("Vui lòng nhập vào lớp") , validators.Length(min=1,max=2)])
    Th_Gioi_tinh = RadioField("Giới tính" , choices=[ ("M" , "Nam") , ("F" , "Nữ") , ("D" , "Khác") ])
    Th_Dia_chi = TextAreaField("Địa chỉ")
    Th_Sdt = IntegerField("Số điện thoại" , [validators.Required("Vui lòng nhập vào số điện thoại") ,validators.Length(min=4, max=15)])
    Th_Email = TextField("Email" , [validators.Required("Vui lòng nhập vào Email") , validators.Email("Vui lòng nhập vào Email") ,validators.Length(min=4, max=30)])
    Th_Confirm = BooleanField('Đồng ý cập nhật thông tin', [validators.InputRequired()])
    Th_Submit = SubmitField("Cập nhật")'''
