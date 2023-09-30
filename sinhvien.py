class SinhVien:
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name
    def in_thong_tin(self):
        print('Day la sinh vien: ',self.name,'ID sinh vien la: ',self.ID)
class SinhVienA(SinhVien):
    def __init__(self,name,ID):
        SinhVien.__init__(self,name,ID)
    def in_thong_tin2(self):
        print('Day la sinh vien truong A ')
sva = SinhVienA('Khuong',202224)
sva.in_thong_tin()
sva.in_thong_tin2()