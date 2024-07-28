meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey", 
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "Bir Şakaya karşılık cevap",
            "SHEESH" : "Onaylamamak",
            "CREEPY" : "Korkunç",
            "AGGRO" : "Agresifleşmek/Sinirlenmek"
}


kullanici_istek = input("Hangi kelimenin anlamını öğrenmek istersin (Kelimeyi Büyük harflerle yaz!)?").upper()


if kullanici_istek in meme_dict.keys():
   print("Girdiğiniz kelimenin anlamı: ", meme_dict[kullanici_istek]) 
else:
    print("Üzgünüm bu sözlükte aradığınız kelime yok :(")
