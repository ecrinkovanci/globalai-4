from datetime import date

sorular = [{"soru":"Türkiye'nin başkenti neresidir?", "cevap": "ankara"},
{"soru":"Bugün ayın kaçı?", "cevap": str(date.today().day) },
{"soru":"Python'ı geliştiren kişi kimdir?", "cevap":"guido van rossum"},
{"soru":"Felsefe Taşı'nı koruyan köpek kaç başlıdır? (rakam ile belirtiniz)", "cevap":"3"},
{"soru":"Bern nerenin başkentidir?", "cevap":"isviçre"},
{"soru":"2006 yılında çıkmış olan Prestij filminin yönetmeni kimdir?", "cevap":"christopher nolan"},
{"soru":"Dan Brow'un Cehennem adlı kitabı İstanbul'da nerede geçmiştir?", "cevap":"yerebatan sarnıcı"},
{"soru":"46 plaka kodu hangi ilimize aittir?", "cevap":"kahramanmaraş"},
{"soru":"Tolkien tarafından yazılan ve Orta Dünya'da geçen kitabın adı nedir?", "cevap":"yüzüklerin efendisi"},
{"soru":"Basketbolda hatalı yürüme olarak da adlandırılan oyun ihlaline ne denir?", "cevap":"steps"}]

score = 0

for i in range(len(sorular)):
    print("Soru", i + 1, ":", sorular[i]["soru"])
    if sorular[i]["cevap"] == input("cevabınız: ").lower():
        score += 10

print("")

if score > 50:
    print("TEBRİKLER! BAŞARIYLA TAMAMLADINIZ.")
else:
    print("BAŞARISIZ OLDUNUZ! YENİDEN DENEYEBİLİRSİNİZ.")


print("\nPuanınız: ", score)
