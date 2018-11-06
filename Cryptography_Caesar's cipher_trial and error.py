encrypted_text1 = """
RW. XMJWQTHP MTQRJX, BMT BFX ZXZFQQD AJWD QFYJ NS YMJ RTWSNSLX, XFAJ ZUTS YMTXJ
STY NSKWJVZJSY THHFXNTSX BMJS MJ BFX ZU FQQ SNLMY, BFX XJFYJI FY YMJ GWJFPKFXY YFGQJ.
N XYTTI ZUTS YMJ MJFWYM-WZL FSI UNHPJI ZU YMJ XYNHP BMNHM TZW ANXNYTW MFI QJKY GJMNSI
MNR YMJ SNLMY GJKTWJ. NY BFX F KNSJ, YMNHP UNJHJ TK BTTI, GZQGTZX-MJFIJI, TK YMJ XTWY
BMNHM NX PSTBS FX F "UJSFSL QFBDJW." OZXY ZSIJW YMJ MJFI BFX F GWTFI XNQAJW GFSI SJFWQD
FS NSHM FHWTXX. "YT OFRJX RTWYNRJW, R.W.H.X., KWTR MNX KWNJSIX TK YMJ H.H.M.," BFX
JSLWFAJI ZUTS NY, BNYM YMJ IFYJ "1884." NY BFX OZXY XZHM F XYNHP FX YMJ TQI-KFXMNTSJI
KFRNQD UWFHYNYNTSJW ZXJI YT HFWWD—INLSNKNJI, XTQNI, FSI WJFXXZWNSL. 

"BJQQ, BFYXTS, BMFY IT DTZ RFPJ TK NY?" 
"""

def decrypt_code(shift):
    alpha = {}
    i = 0
    for c in encrypted_text1:
        alpha[i] = c
        i = i + 1
        
    alpha1 = {}
    for x, y in alpha.items():
        if 'A' <=y<= 'Z':
            if (ord(y) + shift) > ord('Z'):
                alpha1[x] = chr((ord('A')-1) + (ord(y) + shift - ord('Z')))
            else:
                alpha1[x] = chr(ord(y) + shift)
        else:
            alpha1[x] = y
        
    decrypt_text = ''
    for c in alpha1.values():
        decrypt_text = decrypt_text + c
    
    return decrypt_text

decrypt_text = decrypt_code(21)
