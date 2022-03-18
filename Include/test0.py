# region Variabel
def Variabel():
    # Variabel adalah tempat menyimpan data

    #  menaruh / assigmment nilai
    a = 10
    x = 5
    panjang = 1000

    # pemangilan pertama
    print("Nilai a = ", a)
    print("Nilai x = ", x)
    print("Nilai panjang = ", panjang)

    # penamaan
    nilai_y = 15  # dengan menggunakan underscore
    juta10 = 10000000  # ini boleh
    nilaiZ = 17.5  # ini boleh

    # pemanggilan kedua
    print("Nilai a = ", a)
    a = 7
    print("Nilai a = ", a)

    # assignment indirect
    b = a
    print("Nilai b = ", b)
# endregion

# region Tipe Data


def TipeData():
    # a = 10, a adalah variabel dengan nilai 10

    # tipe data: angka satuan (integer)
    data_integer = 1
    print(type(data_integer))
    print(f'Data : {data_integer}, \n- bertipe: {type(data_integer)}')

    # tipe data: angka dengan koma (float)
    data_float = 1.5
    print(type(data_float))
    print(f'Data : {data_float}, \n- bertipe: {type(data_float)}')

    # tipe data: kumpulan karakter (string)
    data_string = 'Pintu'
    print(type(data_string))
    print(f'Data : {data_string}, \n- bertipe: {type(data_string)}')

    # tipe data: biner true/false (boolean)
    data_bool = True
    print(type(data_bool))
    print(f'Data : {data_bool}, \n- bertipe: {type(data_bool)}')

    # tipe data khusus

    # bilangan kompleks
    data_complex = complex(5, 6)
    print(type(data_complex))
    print(f'Data : {data_complex}, \n- bertipe: {type(data_complex)}')

    # tipe data dari bahasa C

    from ctypes import c_double, c_longlong

    data_c_double = c_double(10.5)
    print(type(data_c_double))
    print(f'Data : {data_c_double}, \n- bertipe: {type(data_c_double)}')
# endregion

# region Casting Tipe Data


def casting():
    # merubah dari satu tipe ke tipe lain
    # tipe data = int, float, str, bool
    # INTEGER
    print('=====INTEGER=====')
    data_int = 9
    print('data = ', data_int, ',type = ', type(data_int))

    data_float = float(data_int)
    data_str = str(data_int)
    data_bool = bool(data_int)
    print('data = ', data_float, ',type = ', type(data_float))
    print('data = ', data_str, ',type = ', type(data_str))
    print('data = ', data_bool, ',type = ', type(data_bool))

    # Float
    print('=====FLOAT=====')
    data_float = 9.9
    print('data = ', data_float, ',type = ', type(data_float))

    data_int = int(data_float)
    data_str = str(data_float)
    data_bool = bool(data_float)
    print('data = ', data_int, ',type = ', type(data_int))
    print('data = ', data_str, ',type = ', type(data_str))
    print('data = ', data_bool, ',type = ', type(data_bool))

    # Boolean
    print('=====BOOLEAN=====')
    data_bool = False
    print('data = ', data_bool, ',type = ', type(data_bool))

    data_int = int(data_bool)
    data_str = str(data_bool)
    data_float = float(data_bool)
    print('data = ', data_int, ',type = ', type(data_int))
    print('data = ', data_str, ',type = ', type(data_str))
    print('data = ', data_float, ',type = ', type(data_float))

    # STRING
    print('=====STRING=====')
    data_string = '10'
    print('data = ', data_string, ',type = ', type(data_string))

    data_int = int(data_string)  # string harus angka
    data_bool = bool(data_string)  # false jika string kosong
    data_float = float(data_string)  # string harus angka
    print('data = ', data_int, ',type = ', type(data_int))
    print('data = ', data_bool, ',type = ', type(data_bool))
    print('data = ', data_float, ',type = ', type(data_float))

# endregion


Variabel()
TipeData()
casting()
