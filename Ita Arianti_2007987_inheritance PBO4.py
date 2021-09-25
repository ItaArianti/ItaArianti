class _orang():
    def __init__(self, nama, asal, tgl_lahir, gender):
        self.nama = nama
        self.asal = asal 
        self.tgl_lahir = tgl_lahir
        self.gender = gender

    def tampilan(self):
        print('Nama :',self.nama , '\nAsal : ',self.asal ,'\nTanggal Lahir : ',self.tgl_lahir, '\nGender : ',self.gender)

class _mhs(_orang):
    def __init__(self, nama, asal, tgl_lahir, gender, nim, Prodi, Kelas):
      super().__init__(nama, asal, tgl_lahir, gender)
      self.nim = nim 
      self.Prodi = Prodi
      self.Kelas = Kelas

    def _tampilan_mhs(self):
        print("MAHASISWA")
        print('Nama :',self.nama , '\nAsal : ',self.asal ,'\nTanggal Lahir : ',self.tgl_lahir, '\nGender : ',self.gender, '\nnim : ',self.nim, '\nProdi : ',self.Prodi, '\nKelas : ',self.Kelas)

class _dosen(_orang):
    def __init__(self, nama, asal, tgl_lahir, gender, nik):
      super().__init__(nama, asal, tgl_lahir, gender)
      self.nik = nik 
      
    def _tampilan_dosen(self):
        print("DOSEN")
        print('Nama :',self.nama , '\nAsal : ',self.asal ,'\nTanggal Lahir : ',self.tgl_lahir, '\nGender : ',self.gender, '\nnik :', self.nik)


mahasiswa1 = _mhs('ita','jambi','21/03/2002','P','2007987','SIK','3B')
dosen1 = _dosen('Agus, S.Pd','jember','01/01/1990','L','20000973428')

mahasiswa1._tampilan_mhs()
print("----------------------------------------")
dosen1._tampilan_dosen()