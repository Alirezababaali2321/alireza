from pyrubi import Client 
from re import findall
from pyrubi.types import Message
import random
import time
import re
import requests
import requests 
from bs4 import BeautifulSoup

# تابع برای ارسال درخواست به API هوش مصنوعی
v = [
    "download (3).jpg"
    ,"download (4).jpg"
]
       

# اجرای ربات
url = 'https://www.tgju.org/profile/geram18'
x = requests.get(url)
u = 'https://www.tgju.org/profile/price_dollar_rl'
v = requests.get(u)
b = 'https://www.tgju.org/profile/crypto-bitcoin'
g = requests.get(b)
# لیست پاسخ‌های تصادفی برای "خوبی؟"
good_responses = ["آره، تو چطوری؟", "خداروشکر، تو چخبر؟", "عالی! مرسی که پرسیدی!", "همیشه خوبم، تو چطوری؟"]

# لیست سوالات بازی
questions = [
    "اگر به گذشته برگردی، چه چیزی رو تغییر میدی؟",
    "قدرتی داشتی که می‌تونستی آینده رو ببینی، چیکار می‌کردی؟",
    "بهترین فیلمی که دیدی چیه؟",
    "اگر می‌توانستی یک چیز رو تو دنیا عوض کنی، چی بود؟",
    "دوست داری تو آینده چی‌کار کنی؟"
]
r = [
    "خودتی😁","دالگ خودت👍","یکبار دیگه فحش بدی خودم ریم میززنمت😎","باباته","خودتی","ننته"
]
t = [
"😂👉با این ***دستی ولی جوابتو دادم","درست بگو ربات","لالی","خاک تو سرت بلد نیستی چت کنی","هعی درست بگو ربات"

]
y = [
"😒ها چته","!جونم خوشگلم","وای این باز منو صدا کرد من رفتم","وای بچه ها انقدر از این بدم میاد"
,"😡ها"
]
q = [

    "به تو چه","شینا","شینا جون","نمیخوام بگم"
]
m = [
"تو ان منی","تو زن منی","چبدونم","نمیدونم","نمیخواد بدونی","بچه خوشگل","بچه ساکت گروه","بچه ک..نی"
,"شوتی","خر منی","گاو منی","سگ منی","ان منی","همسر منی"

]
b = [
"به تو چه این کیه😒","به تو ربطی داره ؟😂","به تو ربط نداره😎😂","به من چه به تو چه به اینئ چه"


]
k = [
"1:شانستو😂","2:بد نیست بیا","3:اومد برات","4:هعی بیا","5:ای جان","6:به به عشق کن "
]
s = [
"آخرین دروغی که به پدر خود گفتید و برای آن پول دریافت کردید","شرم آورترین کاری که تا به حال در قرار ملاقات انجام داده اید چه بوده است؟","آیا تا به حال شده که به طور تصادفی با ماشین خود به چیزی (یا شخصی!) برخورد کرده باشید؟","نام کسی را که وانمود کرده اید دوستش دارید، اما در واقع نمی توانید تحمل کنید، نام ببرید.","عجیب ترین نام مستعار شما چیست؟","دردناک ترین تجربه فیزیکی شما چه بوده است؟"
,"آیا تاکنون مزاحم تلفنی شده اید؟ آن را توضیح دهید.","احمقانه ترین کاری که در حمل و نقل عمومی انجام داده اید چیست؟","اگر با یک جن ملاقات کنید، سه آرزوی شما چه خواهد بود؟","اگر بتوانید برای کسی روی زمین به عنوان رئیس جمهور ایالات متحده بنویسید، چه کسی و چرا؟","آیا تاکنون از سوپر مارکت دزدی کرده اید؟"

]
a = [
"امان از دسته این مانکنای جلویه مغازه‌ها امروز دماغ یکیشونو گرفتم برگشت بهم گفت مرض داری؟ نگو صاحب مغازه بود!! 😐",
"اینکه میگن زنای خوشگل گیر مرد های زشت میفتن منظورشون زشت های پولداره تو به خودت نگیر رفیق",
"هیچوقت از روی ظاهر کسی قضاوت نکنینالان مثلا به قیافه سیب‌زمینی میاد انقدر خوشمزه باشه؟",
"حالا گاوداری و مرغداری و پرورش اسب و این چیزا رو خارج شهر می‌سازن قابل درکه برام!اما نمی‌فهمم دیگه چرا دانشگاه‌ها رو خارج شهر می‌سازن؟:|",
"یه چیزی که مدت‌ها نگهش داشتی و دیگه به دردت نمیخوره رو بندازش دور.حالا اگه یک ساعت بعدش همون جنس به کارت نیومد بیا بزن تو گوش من!",
"",

]
z = [
    "Untitled-36.jpg",
    "Call-of-Duty-Mobile-Tips-Cover.jpg"
    ,"call_of_duty_top_games.webp"
    ,"1739283865.225h.jpeg"

]
d = [
"Hayedeh - Badeh Forush.mp3",
"Hayedeh - Afsaneyeh Hasti.mp3"
,"Shadmehr Aghili - Tamasha [320].mp3"
,"Shadmehr Aghili - Chera Too Jangi [128].mp3"
,"Shadmehr Aghili - Daste Man Nist [320].mp3"
,"Shadmehr Aghili - Bi Ehsas [320].mp3"
,"Shadmehr Aghili - Door Shodi [320].mp3"
,"Shadmehr Aghili - Khaabe Khosh [320].mp3"
,"1-06 Afsaneh Hasty (1).mp3"
,"1-07 Parishoon.mp3"
,"1-08 Arosak.mp3"
,"1-09 Ye Rooz.mp3"
,"2-01 Nagoo Nemiyam.mp3"
,"1-01 Shanehayat.mp3"
,"1-02 Asheghtarin.mp3"
,"1-03 Ey Zendegi Salam.mp3"
,"1-04 Sayeh Eshgh.mp3"
,"Mahasti - Ghesehe Ma.mp3"
,"Mahasti - Hanooz Ham Dooset Daram.mp3"
,"Mahasti - Dou Rangi.mp3"
,"Mahasti - Bazicheh.mp3"
,"Mahasti - Bazicheh (1).mp3"
,"Poori - Baalaam (128).mp3"
,"Poori - Man Ba To (128).mp3"
,"Poori - Man Kardam (128).mp3"
,"Poori - Yaadet Nare (128).mp3"
,"Behem Dande Midi (320) (1).mp3"
,"Ramin Tajangi - Kalafee (320) (1).mp3"
,"Dardet Dmin Ghalbam (320) (1).mp3"
,"Behem Dande Midi (320) (2).mp3"
,"Ramin Tajangi - Shahrag (320).mp3"
,"Ramin Tajangi - Kalafee (320) (2).mp3"
,"Ramin Tajangi Ft Mohammad Amiri _ Divane (320).mp3"
]
i = [
"Behzad Leito – Dardesar [320].mp3"
,"Behzad Leito – Dardesar [320] (1).mp3"
,"Behzad Leito - Mamacita [320].mp3"
,"Sepehr Khalse - Siyah Mese Barf [320].mp3"
,"Sepehr Khalse - Salibi [320].mp3"
,"Zedbazi - Yakh.mp3"
,"Wantons - Pas Man Chi [320].mp3"
,"Wantons - Fada Saret [320].mp3"
,"Alireza JJ - Sahme Mani [320].mp3"
,"Alireza JJ - Gole Sangam [320].mp3"
,"Epicure - Gahi Vaghta [320].mp3"
,"Epicure - Begoo Yadete [320].mp3"
,"Gdaal & Madgal - Banafsh [320].mp3"
,"Erfan - Montazer [320].mp3"
,"Erfan - Mano Natarsoon [320].mp3"
,"Amir Tataloo - Gorg [320].mp3"
,"Ho3ein - 12 Be Bad [320].mp3"
,"Reza Pishro - Divoone 2 Remix [320].mp3"
,"Reza Pishro - Niloofar Abi [320].mp3"
,"Gdaal - Shaghayegh [320].mp3"
]
n = [

    "VID_20250209_101553_821 (1).mp4"
    ,"Screenrecorder-2025-02-09-21-38-40-877 (1).mp4"
    ,"VID_20250209_114617_789.mp4"
    ,"VID_20250209_115958_508.mp4"
      
]
u = [
    "1739284731.727h.jpeg"
    ,"1739284725.384h.jpeg"
    ,"1739284713.982h.jpeg"
    ,"1739284721.366h.jpeg"
    ,"1739284707.926h.jpeg"
    ,"1739284690.669h.jpeg"
    ,"1739284687.316h.jpeg"
    ,"1739284679.608h.jpeg"
    ,"1739284674.708h.jpeg"
    ,"1739284668.766h.jpeg"
    ,"1739284663.845h.jpeg"
    ,"1739284658.796h.jpeg"
    ,"1739284644.281h.jpeg"
    ,"1739284634.185h.jpeg"
    ,"1739284623.545h.jpeg"
    ,"1739284613.301h.jpeg"
    ,"1739284603.444h.jpeg"
    ,"1739284597.759h.jpeg"
    ,"1739284590.148h.jpeg"
    ,"1739284582.237h.jpeg"
    ,"1739284568.294h.jpeg"
    ,"1739284560.779h.jpeg"
    ,"1739284556.005h.jpeg"
    ,"1739284545.987h.jpeg"
    ,"1739284539.229h.jpeg"
    ,"1739284533.131h.jpeg"
    ,"1739284740.558h.jpeg"
    ,"1739284746.913h.jpeg"
    ,"1739284765.173h.jpeg"
    ,"1739284775.751h.jpeg"
    ,"1739284782.666h.jpeg"
    ,"1739284786.102h.jpeg"
    ,"1739284797.303h.jpeg"
    ,"1739284808.346h.jpeg"
    ,"1739284814.371h.jpeg"
    ,"1739284817.895h.jpeg"
    ,"1739284825.487h.jpeg"
    ,"1739284829.405h.jpeg"
    ,"1739284842.387h.jpeg"
    ,"1739284849.185h.jpeg"
    ,"1739284857.244h.jpeg"
    ,"1739284863.568h.jpeg"
    ,"1739284867.984h.jpeg"
    ,"1739285604.287h.jpeg"
    ,"1739285615.614h.jpeg"
    ,"1739285623.001h.jpeg"
    ,"medium_0ed9ab47-29cf-416e-8e4d-8799d98abece.webp"
    ,"medium_0fe2f269-34db-4652-aeb0-d2d8d6a67d80.webp"
    ,"medium_4670b0c5-9c9d-47c7-81f8-364db081f4ea.webp"
    ,"medium_7dbfedbe-ecce-4155-bed6-c6c106b67020.webp"
    ,"medium_fa4f6766-1655-4385-913a-85a86bfa83b5.webp"
    ,"medium_94708616-4413-4ae3-9a30-2236a2537691.webp"
    ,"medium_2c48aebb-f71f-41ad-8682-28c408472bd3.webp"
    ,"medium_f95c73ca-bd0d-4e4f-ad65-8f24790239b8.webp"
    ,"medium_9b2d59d9-cc42-4284-9d4b-4fdf5ae8c346.webp"
    ,"medium_321c37c0-f151-4a96-b355-221098b8fb2c.webp"
    ,"medium_5694c8cc-5c58-46a4-b945-0637a95bad9c.webp"
    ,"medium_8d16c1f7-2df5-438e-b360-aa476fdb53a1.webp"
    ,"medium_b9ba2749-15d6-4b18-a0ec-002bd8796c13.webp"
    ,"medium_aad7e5f5-303f-489e-bbb7-07e5b290595f.webp"
    ,"medium_32290a5a-7683-48bd-a52d-91e8a39effa5.webp"
    ,"medium_c32281da-45ac-454e-83f1-93a502d6c504.webp"
    ,"medium_1f12f658-fc01-4adc-ac98-ec0149ca2274.webp"
    ,"medium_2b458f75-b1ac-460b-8cb0-edb1ea0bb732.webp"
    ,"medium_44b92b7a-78c7-4815-b473-b1685db25cef.webp"
    ,"medium_821cfd5d-b172-47f9-8457-cea18efe9a81.webp"
    ,"medium_bd924603-0344-459f-8923-bb8888cd90bd.webp"
    ,"medium_1491411c-0ded-46cd-837a-abb3dddfe005.webp"
    ,"medium_70f77330-72b8-45af-8344-bdc23a2308a6.webp"
    ,"medium_563d4198-4d49-46a3-8abf-d2bf4fa72e63.webp"
    ,"medium_b338e1c6-4c2c-4c92-bb88-777278b6d618.webp"
    ,"medium_91e72f64-23ca-4434-8da4-7129c2c13f3d.webp"
    ,"medium_96898ec9-d64f-4f55-b0bc-77d9de3815d7.webp"
    ,"medium_17f58965-1e84-4c91-9593-aa9c662dc6ac.webp"
    ,"medium_d665c91b-42d9-4a39-b9fb-698f602f01d8.webp"
    ,"medium_67f113e6-d2c9-41fc-954f-6d349699e27d.webp"
    ,"medium_7472ae48-bc30-40f5-a9db-92593ce12a38.webp"
    ,"medium_4e076b5d-f7a7-48c7-8b2d-2d994c8b0ce7.webp"

    ,"medium_89739265-7218-46cc-aeff-7e52981e39b3.webp"
    ,"medium_a42de63d-d3c0-46cf-b53c-4cb6ce762869.webp"
    ,"medium_051b3b12-a40b-4a75-adf2-978a5e81751a.webp"
    ,"medium_a7c0da03-3472-4fde-a99b-3e595bd3b4ee.webp"
    ,"medium_ff597567-7be3-4ea3-b10a-8aa78aff92c2.webp"
    ,"medium_5d484efe-87a2-40b1-8b4a-ede048a7b2c8.webp"
    ,"medium_dcc41a79-3301-4f92-a194-860c289629a8.webp"
    ,"medium_340dd549-12af-4f1c-94cf-8de242359efa.webp"
  
]
c = [

    "image.jpeg"
    ,"image (1).jpeg"
    ,"image (2).jpeg"
    ,"IMG_20250214_074639_848.jpg"
    ,"IMG_20250214_074643_266.jpg"
    ,"IMG_20250214_074645_709.jpg"
    ,"IMG_20250214_074646_013.jpg"
    ,"IMG_20250214_074637_144.jpg"
    ,"IMG_20250214_074646_042.jpg"
    ,"IMG_20250214_074648_075.jpg"
    ,"IMG_20250214_074648_698.jpg"
    ,"IMG_20250214_074648_596.jpg"
    ,"IMG_20250214_074648_125.jpg"
    ,"IMG_20250214_074648_544.jpg"
    ,"IMG_20250214_074821_753.jpg"
    ,"IMG_20250214_074821_395.jpg"
    ,"IMG_20250214_074821_392.jpg"
    ,"IMG_20250214_074821_289.jpg"
    ,"IMG_20250214_074821_841.jpg"
    ,"IMG_20250214_074821_597.jpg"
    ,"IMG_20250214_074821_314.jpg"
    ,"IMG_20250214_074826_366.jpg"
    ,"IMG_20250214_074821_924.jpg"
    ,"IMG_20250214_074821_823.jpg"
    ,"IMG_20250214_074821_519.jpg"
    ,"IMG_20250214_074822_084.jpg"
    ,"IMG_20250214_074826_385.jpg"
    ,"IMG_20250214_074832_117.jpg"
    ,"IMG_20250214_074831_767.jpg",
    "IMG_20250214_074831_906.jpg"
    ,"IMG_20250214_074832_276.jpg"
    ,"IMG_20250214_074826_019.jpg"
    ,"IMG_20250214_074831_771.jpg"
    ,"IMG_20250214_074831_931.jpg"
    ,"IMG_20250214_074838_952.jpg"
    ,"IMG_20250214_074839_026.jpg"
    ,"IMG_20250214_074838_610.jpg","IMG_20250214_074838_756.jpg"
    ,"IMG_20250214_074846_493.jpg"
    ,"IMG_20250214_074847_066.jpg"
    ,"IMG_20250214_074846_874.jpg"
    ,"IMG_20250214_074847_040.jpg"
    ,"IMG_20250214_074846_962.jpg"
    ,"IMG_20250214_074847_243.jpg"
    ,"IMG_20250214_074847_161.jpg"
    ,"IMG_20250214_074847_002.jpg"
    ,"IMG_20250214_074846_483.jpg"
    ,"IMG_20250214_074847_187.jpg"
    ,"IMG_20250214_074850_869.jpg"
    ,"IMG_20250214_074850_564.jpg"
    ,"IMG_20250214_074850_525.jpg"
    ,"IMG_20250214_074850_717.jpg"
    ,"IMG_20250213_075104_607.jpg"
    ,"IMG_20250213_075104_658.jpg"
    ,"IMG_20250213_075104_055.jpg"
    ,"IMG_20250213_075104_695.jpg"
    ,"IMG_20250213_075104_363.jpg"
    ,"IMG_20250213_075117_708.jpg"
    ,"IMG_20250213_075118_083.jpg"
    ,"IMG_20250213_075118_191.jpg"
    ,"IMG_20250213_075117_413.jpg"
    ,"IMG_20250213_075117_717.jpg"
    ,"IMG_20250213_075125_386.jpg"
    ,"IMG_20250213_075124_624.jpg"
    ,"IMG_20250213_075253_292.jpg"
    ,"IMG_20250213_075255_245.jpg"
    ,"IMG_20250213_075317_122.jpg"
    ,"IMG_20250213_075326_432.jpg"
    ,"IMG_20250210_163002_246.jpg"
    ,"IMG_20250210_163002_408.jpg"
    ,"IMG_20250210_163002_115.jpg"
    ,"IMG_20250214_081837_263.jpg"
    ,"IMG_20250214_081837_263.jpg"
    ,"IMG_20250214_081839_435.jpg"
    ,"IMG_20250214_081839_488.jpg"
    ,"IMG_20250214_081839_299.jpg"
    ,"IMG_20250214_081839_147.jpg"
    ,"IMG_20250214_081839_216.jpg"
    ,"IMG_20250214_081839_439.jpg"
,"IMG_20250213_230353_709.jpg"
,"IMG_20250213_225429_671.jpg"
,"IMG_20250213_225430_242.jpg"
,"IMG_20250213_225430_633.jpg"
,"IMG_20250213_225433_717.jpg"
,"IMG_20250213_225433_284.jpg"
,"IMG_20250213_225435_242.jpg"
,"IMG_20250213_184122_586.jpg"
,"IMG_20250213_184122_945.jpg"
,"IMG_20250213_184122_374.jpg"
,"IMG_20250213_184122_684.jpg"
,"IMG_20250213_094046_942.jpg"
,"IMG_20250213_094044_174.jpg"
,"IMG_20250214_101050_802.jpg"
,"IMG_20250214_101051_289.jpg"
,"IMG_20250213_165501_946.jpg"
,"-2147483648_-225949.jpg"
,"IMG_20250211_094550_818.jpg"
,"IMG_20250214_095650_712.jpg"
,"IMG_20250214_095651_425.jpg"
,"IMG_20250214_095650_445.jpg"
,"IMG_20250213_212353_290.jpg"
,"IMG_20250213_212353_870.jpg"
,"IMG_20250213_212352_941.jpg"
,"IMG_20250213_212353_617.jpg"
,"IMG_20250213_184436_891.jpg"
,"IMG_20250213_184436_990.jpg"
,"IMG_20250214_081837_196.jpg"
,"IMG_20250213_100215_695.jpg"
,"IMG_20250213_100216_351.jpg"
,"IMG_20250213_100220_739.jpg"
,"IMG_20250212_165247_853.jpg"
,"IMG_20250212_165247_812.jpg"
,"IMG_20250212_165248_375.jpg"
,"IMG_20250212_102450_547.jpg"
,"IMG_20250212_102450_974.jpg"
,"IMG_20250212_102451_090.jpg"
,"IMG_20250212_102451_471.jpg"
,"IMG_20250212_102451_303.jpg"
,"IMG_20250212_102451_077.jpg"
,"IMG_20250212_102451_397.jpg"
,"1739521667.315h.jpeg"
,"1l2fb7pn.jpeg"
,"1739521683.9h.jpeg"
,"1739521688.603h.jpeg"
,"1739521693.938h.jpeg"
,"1739521700.232h.jpeg"
,"1739521725.64h.jpeg"
,"1739521730.964h.jpeg"
,"1739521737.714h.jpeg"
,"1739521744.038h.jpeg"
,"1739521755.137h.jpeg"
,"1739521759.96h.jpeg"
,"1739521764.651h.jpeg"
,"1739521768.017h.jpeg"
,"1739521772.836h.jpeg"
,"1739521778.06h.jpeg"
,"1739521815.166h.jpeg"
,"1739521819.114h.jpeg"
,"1739521824.632h.jpeg"

]
f = [
"‌لطفن در مصرف شعور اصراف کنید🤧 -!"
,"‌‌روزگارمیگذره ، ولی‌ از روت عزیزم!🫤"
,"   حضور ما باعث فشار خیلیاست!"
,"‌من برای آنچه هنوز با تو تجربه نکرده ام دلتنگم."
,"#تیکه😹‌من بد اخلاق نیستم فقد لازم نمیبینم با هر هَوَلے خوش اخلاق باشم..! 🤫"
,"‌مهم نیست چقد سخته ، من میرسم به جایی که میخام!🫡💯"
,"‌‌آدما زمانے ترسناڪ میشن که رازهاتو بهشون گفتے !)"
,"‌ بتونن ، میخرنت ،،، نتونن ، میفروشنت..."
,"‌ترجیح میدم سکوت کنم ، چون حرف زدن هیچیو تغییر نمیده."
," بودن به پارتنر خیلی باکلاسه ، جدی میگم! 😉👌"
,"#تیکه 😹پاسخی نسبت به مشکلاتم جز دانلود سریال ندارم.🗿"
,"‌آدم تا از دست نده قدر نمیدونه🙏🏼!!"
,"‌‌دق‍‌ی‍‌ق‍‌ا ه‍‌م‍‌ون‍‌ی ت‍‌ن‍‌ه‍‌ام‍‌ون گ‍‌ذاش‍‌ت ک‍‌ه ش‍‌ری‍‌ک ت‍‌ن‍‌ه‍‌ای‍‌ی ه‍‌ام‍‌ون ب‍‌ود ؛)🖤🦋"
,"‌‌شخصیت و احترامت رو به احساساتت نفروش!"
,"خاص بودن پيشكش ، آدم باش ! 😪🖖🏼"
,"#تیکه😹با بعضيا حرف زدن افت داره واسه ما :)🤞🏼‌"
,"‌دردم اینه که درکت به دردم نمیرسه. . !"
]
# متغیر برای بررسی وضعیت ربات (فعال یا خاموش)
is_bot_active = True

# تابع برای اجرای ربات
def run_bot():
    client = Client("your-bot-auth-token")

    @client.on_message()
    def handle_message(message: Message):

        global is_bot_active
        try:
            text = message.text
            guid = message.object_guid
            message_id = message.message_id  # دریافت ID پیام برای ریپلای
            
           
            if not text:
                client.send_text(guid, "لطفاً یک متن وارد کنید.")
                return

            # چک کردن فرمان خاموش کردن ربات توسط ادمین
            if text.strip() == "ربات خاموش":
                is_bot_active = False
                client.send_text(guid, "ربات خاموش شد.", message_id)
                return

            # اگر ربات خاموش باشد، هیچ پاسخی ندهد
        

            # ✅ ریپلای روی پیام "سلام" و پاسخ عادی
            if text.strip() == "سلام":
                client.send_text(guid, "باز این اومد من رفتم😁", message_id)
                return
            if "از طریق لینک دعوت به گروه پیوست" in text:
                # ابتدا پاسخ به سوال
                # سپس خوش‌آمدگویی
                client.send_text(guid, "خوش آمدی گویی! 😊", message_id)
                return
            
            # ✅ ریپلای روی پیام "خوبی؟" و پاسخ تصادفی
            if text.strip() in ["خوبی", "حالت چطوره؟", "چطوری؟"]:
                response = random.choice(good_responses)
                client.send_text(guid, response, message_id)
                return

            # ✅ ارسال تصویر یا گیف در پاسخ به "چقدر خفن" و ریپلای روی همون پیام
            if text.strip() == "چقدر خفن":
                media_url = "عکس-خنده-دار-12.jpg.webp"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() == "طنز":
                media_url = "چرا نمیخوابید شما طنز.gif"
                client.send_gif(guid, media_url, message_id)
                return
            if text.strip() == "خستم":
                media_url = "گیف خستم.gif"
                client.send_gif(guid, media_url, message_id)
                return
            
            if text.strip() in ["فحش", "دالگ مجمع", "دالگ خیز"]:
                response = random.choice(r)
                client.send_text(guid, response, message_id)
                return
            if text.strip() in ["اره","ار"]:
                client.send_text(guid, "اجر پاره", message_id)
                return
            if text.strip() in [  "ربان", "ریات ","رتات","رتاب","زبت","ربت","زبات"]:
                response = random.choice(t)
                client.send_text(guid, response, message_id)
                return
            if text.strip() in ["شینا", "ربات", "عشقم ","خوشگلم","جیگرم"]:
                response = random.choice(y)
                client.send_text(guid, response, message_id)
                return
            # ✅ بازی پرسش و پاسخ تصادفی با ریپلای
            if text.strip() in ["یه سوال بپرس", "بازی کنیم", "سوال"]:
                question = random.choice(questions)
                client.send_text(guid, question, message_id)
                return
            if text.strip() in ["اسمت چیه", "نام ربات", "اسم ربات"]:
                question = random.choice(q)
                client.send_text(guid, question, message_id)
                return
         
            if text.strip() in ["شبت بخیر", "شب بخیر", "شب خوش"]:
                media_url = "images (1).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["صبح", "صبح بخیر", "صبحت "]:
                media_url = "images.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() == "گروه را ترک کرد":
                client.send_text(guid, "به درک برای گروه ارزشی نداشت", message_id)
                return
            if text.strip() == "از طریق لینک دعوت به گروه پیوست":
                client.send_text(guid, "سلام خوشگلم به گروه تست ربات خوش اومدی فحش ندی که خودم ریمت میکنم", message_id)
                return
           
            if text.strip() in ["سازنده ربات","تورو کی ساخته","کی ساختت","ربات کی تورو ساخته","تو کی","سازندت کیه"]:
                client.send_text(guid, "سازنده:علیرضا باباعلی          ❤️😒😎               ", message_id)
                return
         
                client.send_music(guid, media_url, message_id)
                return
            if text.strip() == "عه":
                client.send_text(guid, "بخدا", message_id)
                return
            if text.strip() == "چرا":
                client.send_text(guid, "چون چسبیده به راه😎😒", message_id)
                return
            if text.strip() in ["واقعا","جدی","دروغ میگی","دروغگو","دروغ نگو"]:
                client.send_text(guid, "جان تو", message_id)
                return
            if text.strip() in ["مشکوکی","مشکوک","مشکوک میزنی","مشکو","میزنی"]:
                client.send_text(guid, "عمت مشکوکه😡", message_id)
                return
            if text.strip() in ["تو رباتی","تو ربات نیستی","تو ربات هستی","ایا رباتی","انگار ربات نیستی"]:
                client.send_text(guid, "تنها کسی که اینجا رباته منم افتاد😡👌", message_id)
                return
            if text.strip() in ["نیون","لوپ بات","لوپ","نیون بات","ربات نیون","پاسکال","ربات پاسکال","پاسکال بهتره"]:
                client.send_text(guid, " اونا همش باگ دارند اسم اونارو نیار من از همشون بهترم افتاد یا بندازم👍😡👍", message_id)
                return
            if text.strip() == "نخیر":
                media_url = "images (2).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() == "خسته شدی":
                client.send_text(guid, "اره خیلی میشه خاموشم کنی😩", message_id)
                return
            if text.strip() == "ریدم":
                client.send_text(guid, "ریدی که ریدی به من چه😎", message_id)
                return
            if text.strip() in ["ربات میخوام","منم از این رباتا میخوام","منم ربات میخوام","منم ربات میخوام برای گپم","ربات میخوام منم"]:
                client.send_text(guid, "بیا منو ببرم رایگان با صاحبم علیرضا هماهنگ کن", message_id)
                return
            if text.strip() in ["لینک گروه","لینک گروه رو بدید","لینک","لینک گپ","لینک گپ رو میدید"]:
                client.send_text(guid, " این لینک گپ https://rubika.ir/joing/HHBBDHII0YNTLRSDCGOIQHJQHDNTRCEY اینم لینک کانال @shina_bot", message_id)
                return
            if text.strip() == "اصل بده":
                client.send_text(guid, "شینا 5 ساله از تهران", message_id)
                return
            if text.strip() in [ "غمگینم","غم","غمگین","غم انگیز"]:
                media_url = "food-gif(35).gif"
                client.send_gif(guid, media_url, message_id)
                return
            if text.strip() in [ "ای وای","واای","وای","وایییییییی"]:
                media_url = "images (3).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "س","سل","سلا","سلام","سلاک"]:
                media_url = "32483626-8473-b__7927 (1).webp"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "بخند","نخند","خنده","میخندی"]:
                media_url = "32483626-8473-b__7927 (1).webp"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["😂","😂😂","😂😂😂","😂😂😂😂","😂😂😂😂😂","😂😂😂😂😂😂","😂😂😂😂😂😂😂","😂😂😂😂😂😂😂😂","😂😂😂😂😂😂😂😂😂"]:
                client.send_text(guid, "نخند مسواک گرون شده😂", message_id)
                return
            if text.strip() in ["😡","😡😡","😡😡😡","😡😡😡😡","😡😡😡😡😡","😡😡😡😡😡😡😡😡😡","😡😡😡😡😡😡","😡😡😡😡😡😡😡😡😡😡😡😡😡😡","😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡😡"]:
                client.send_text(guid, "جون عصبانی میشی جذابتر میشی", message_id)
                return
            if text.strip() in ["سورس میخوام","سورستو بده","سورس ربات میخوام","سورس ربات مدریت میخوام","سورس ربات گروه میخوام"]:
                client.send_text(guid, "با صاحبم علیرضا صحبت کن من هیچکارم❤️😎", message_id)
                return
            if text.strip() in ["هعی","هعی روزگار","روزگار بدیه","حوصلم","حوصلم سر رفته","حالم بده","حالم خوبی نیست"  ,"حالم خوب نی","حالم خوش نستی" ,"حالم خوش نی"  ]:
                client.send_text(guid, "چته پاشو قر بده حالت خوب میشه", message_id)
                return
            if text.strip() in [ "میگما","بگو بینم","بگم","نمیگم","بگو"]:
                media_url = "giphy.gif"
                client.send_gif(guid, media_url, message_id)
                return
            if text.strip() in [ "سلام دنیا","سلام","س","سل","سلا","سلام خدا"]:
                media_url = "images (4).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["من کیم", "من کی هستم", "من کیستم"]:
                question = random.choice(m)
                client.send_text(guid, question, message_id)
                return
            if text.strip() in ["این کیه", "این کی هست", "تو کی", "تو کی هستی", "کیستی", "تو کیی"]:
                question = random.choice(b)
                client.send_text(guid, question, message_id)
                return
            if text.strip() in ["منم","من","ان","من نمیخوام","من میخوام","منم میخوام","من چی" ]:
                client.send_text(guid, "خب به انم 😎🤣😘", message_id)
                return
            if text.strip() in ["رل میخوام","رل","رل پی" ]:
                client.send_text(guid, "به من چه برو پیدا کن", message_id)
                return
            if text.strip() in ["ربات جون","رباتعلی","رباتی","ربات جونم","ربا" ,"رباط" ,"سلطان","ستون","ستونم"]:
                client.send_text(guid, "!😒جونم خوشگلم", message_id)
                return
            if text.strip() in ["منو چقدر دوس داری","منو چقدر دوس داری؟","منو دوست داری","منو دوست داری","دوسم داری"   ]:
                client.send_text(guid, "خیلی دوست دارم تو چی؟🤣", message_id)
                return
            if text.strip() in ["نه","نه نمیخوام" ,"نمیدم" ]:
                client.send_text(guid, "😒نه و نکمه", message_id)
                return
            if text.strip() in ["ای ادم زرنگ","خودتی","زرنگ","ادم"  ]:
                client.send_text(guid, "خیلی دوست دارم تو چی؟🤣", message_id)
                return    
            if text.strip() in [ "با منی؟","بامنی","باکی هستی","باکی","باکیی","باکی؟"]:
                media_url = "02-08-c36-2419.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس اقا رو نشون بده","عکس خامنه ای","خامنه ای","عکس اقا","اقا امام","اما خامنه ای"]:
                media_url = "300px-NUR00006.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس هایده","هایده"]:
                media_url = "download.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس معین","معین"]:
                media_url = "download (1).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس ابی","ابی"]:
                media_url = "1359327_560.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس مهستی","مهستی"]:
                media_url = "download (2).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس شادمهر","شادمهر"]:
                media_url = "download (3).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس گادپوری","گاد پوری","پوری بالام"]:
                media_url = "255555.webp"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس تتلو","امیرتتلو","تتلو"]:
                media_url = "download (4).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in [ "عکس پیشرو","رضا پیشرو","پیشرو","خدای رپ","بهترین رپر"]:
                media_url = "download (5).jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["هوا چطوره","هاوا چطوره","مستر هوا چطوره" ]:
                client.send_text(guid, "عالیییییییییی", message_id)
                return
            if text.strip() in ["درود" ]:
                client.send_text(guid, "درود برتو ممنونم که از کلمات ایرانی استفاده میکنید!❤️😘", message_id)
                return
            if text.strip() in ["اع" ]:
                client.send_text(guid, "اره👍😊", message_id)
                return
            if text.strip() in ["چند سالته" ]:
                client.send_text(guid, "919", message_id)
                return
            if text.strip() in ["جون","جان","ای جان" ,"ای جانم"  ,"شینا جان" ,"شینا جون"]:
                client.send_text(guid, "لاپات بادمجون😂", message_id)
                return
            if text.strip() in ["بزن سلامتی","سلامتی","پیک اخر","سلامتی خودم و خودت" ]:
                client.send_text(guid, "🥂سلامتی خیار نه بخاطر خ بخاطر یارش😒😎", message_id)
                return
            if text.strip() in ["جون تو","جون این","جون خودم" ]:
                client.send_text(guid, "جون خودت چرا این😂", message_id)
                return  
            if text.strip() in ["افرین","دمت گرم","ممنون" ,"مرسی"]:
                client.send_text(guid, "ایییییییییییی😘😉", message_id)
                return           
            if text.strip() in ["ریاضی","ریاضیات","کتاب ریاضی"]:
                client.send_text(guid, "از بچگی علاقه ای به ریاضی نداشتم الانم نمیتونم سوالتو جواب بدم😂", message_id)
                return         
            if text.strip() in ["بای","خداحافظ","خدانگهدار","خدافظ"]:
                client.send_text(guid, "خداحافظ جیگر❤️😘", message_id)
                return     
            if text.strip() in ["هیچی","هیچ","هیچیی"]:
                client.send_text(guid, "هیچی نداریم اینجا افتاد 🥂😎", message_id)
                return    
            
            if text.strip() in ["اخطار!!"]:
                client.send_text(guid, "اخطار1از3                  کاربر....لطفا کار خودرا دیگر تکرار نکنید", message_id)
                return  
            if text.strip() in ["خوش"]:
                client.send_text(guid, "سلام سلطان به گروه خوش اومدی دوستان خودتم دعوت کن تو که اومدی❤️😘", message_id)
                return  
            
            if text.strip() in ["بی ادب","بی تربیت","ربات زشته","زشته"]:
                client.send_text(guid, "خودتی بیشعور 😒", message_id)
                return  
            if text.strip() in ["ربات جقی","ربات کونی","ربات خراب","ربات مادرجنده","مادرجنده","دیوس"]:
                client.send_text(guid, "خودتی 👉😎", message_id)
                return  
            if text.strip() in ["ناموصن","ناموس","ناموسن","خدایی","تروخدا","خداوکیلی"]:
                client.send_text(guid, "اره جان تو😂", message_id)
                return  
            
            if text.strip() in ["ربات تاس", "تاس", "تاس بنداز", "تاس بینداز", "ربات تاس بنداز", "شینا تاس", "شینا تاس بنداز"]:
                question = random.choice(k)
                client.send_text(guid, question, message_id)
                return
            if text.strip() in ["بیا بازی","بازی","حوصلم","حوصلم سر رفته","خستم","خسته ام"]:
                client.send_text(guid, "بیا بازی جرات حقیقت !🥂", message_id)
                return 
            if text.strip() in ["جرات", "جراات", "جرا","حقیقت", "حقیق", "حیقیت میگم"]:
                question = random.choice(s)
                client.send_text(guid, question, message_id)
                return
            
            if text.strip() in ["عاطفه","عاطفههه"]:
                client.send_text(guid, "وای اسمشو نیار🍑", message_id)
                return 
            
            if text.strip() in ["جوک","شینا یک جوک بگو","ربات جوک بگو","شینا جوک بگو","جوک بگو"]:
                question = random.choice(a)
                client.send_text(guid, question, message_id)
                return
            if text.strip() in ["جوک تصویری"]:
                media_url = "juke-2.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["بیا","بیاا"]:
                client.send_text(guid, "من نمیام تو بیا", message_id)
                return 
            if text.strip() in ["بگو","نه بگو"]:
                client.send_text(guid, "وای اسمشو نیامن مثل تو بی تربیت نیستم هرچی بیاد دهنم بگم😎🥂", message_id)
                return 
            if text.strip() in ["بیاپی","بیا پیوی","بیا پی وی","بیا پی"]:
                client.send_text(guid, "نمیام تو بیا😎🍑👍", message_id)
                return 
            if text.strip() in ["الوو","الووو","الو","الوووو","الووووو","الوووووو"]:
                client.send_text(guid, "ها چته هی میگی الو😒🍑", message_id)
                return 
            if text.strip() in ["تو رباتی","تو ادمی","ایا تو رباتی","رباتی؟","ایا تو رباتی؟","تو ربات نیستی"]:
                client.send_text(guid, "ربات هستم افتاد 😎😒", message_id)
                return 
            if text.strip() in ["سیک","سیکتیر","داشاماق","سیکترین","برو گمشو","نمیام"]:
                client.send_text(guid, "اینجا از این حفا نداریم 😒", message_id)
                return 
            if text.strip() in ["رفت","رفتی","رفتین","رفتش","نرو","برو"]:
                client.send_text(guid, "وا چرا 🤨😂👌", message_id)
                return 
            if text.strip() in ["به به","بهبه","خوب","خوبه","خیلی","به"]:
                client.send_text(guid, "چیه خوشت اومده ازم😂🥂❤️", message_id)
                return 
            if text.strip() in [ "شاه ایران","محمد رضا شاه","پهلوی","شاه پهلوی","شاه","ایران"]:
                media_url = "Mohammad_Reza_Pahlavi_2.jpg"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["اوک","اکی","اک","اوکی","اوکیه","اوکی شد","اوکس"]:
                client.send_text(guid, "فارسی را پاس بداریم😎❤️🥂", message_id)
                return 
            if text.strip() in ["پول","پول بده","پول میخوام","پول لازمم","دلار","شینا پول بده","ربات پول بده","ربات پول میخوام","شینا پول میخوام"]:
                client.send_text(guid, "💸برو کار کن پول دربیار پول از من نخواه من از خودت لازم ترم😂🤑", message_id)
                return 
            if text.strip() in ["چقد بی ادبی","بی ادب","چقدر بی ادبی","شینا چقدر بی ادبی","شینا چقدر بی ادبه","بی تربیت","شینا چقدر بی تربیته","ربات چقد بی ادبه","ربات بی ادب"]:
                client.send_text(guid, "💸برو کار کن پول دربیار پول از من نخواه من از خودت لازم ترم😂🤑", message_id)
                return 
            if text.strip() in ["دانلود موزیک","اهنگ","درخواست اهنگ","درخواست موزیک","حالم","اهنگ بده","اهنگ میخوام","درخواست موزیک","اهنگ","موزیک","موزیک بده","اهنگ نمیده","اهنگ میده","اهنگ نمیده؟"]:
            
                question = random.choice(d)
                client.send_text(guid, "این کار ممکن است بین 5 تا 20 ثانیه طول بکشد منتظر باشید❤️🥂😎", )
           
                client.send_music(guid, question, message_id)
                return
            

            
            if text.strip() in [ "عجب","عجیب","عجیبه","عجبه"]:
                media_url = "1711219726041-inshot_20240323_231820525.gif"
                client.send_gif(guid, media_url, message_id)
                return
            if text.strip() in [ "خنده","خنده دار","خند","بخند","طنز","درخواست طنز"]:
                media_url = "e1560414e9f0c895687e81c0e15fdf3652883740-240p.mp4"
                client.send_video(guid, media_url, message_id)
                return
            if text.strip() in ["لیست دستورات","دستورات","راهنما","لیست دستور"]:
                client.send_text(guid, "فعلا لیست دستوری تعیین نشده", message_id)
                return  
            if text.strip() in ["درخواست رپ","رپ","رپ میخوام","شینا رپ میخوام","شینا رپ","رپ بده","ربات رپ میخوام"]:
            
                question = random.choice(i)
                client.send_text(guid, "این کار ممکن است بین 5 تا 20 ثانیه طول بکشد منتظر باشید❤️🥂😎", message_id)
           
                client.send_music(guid, question, message_id)
                return
            if text.strip() in ["ربات سجاد","پاسکال","ربات پاسکال"]:
                client.send_text(guid, "اسم اون رو نیار اون کع خماره😂😎😒🍑", message_id)
                return 
            if text.strip() in ["شینا اسمت چیه","شینا اسمت","ربات اسمت چیه"]:
                client.send_text(guid, "من اسم باباتو دارم پس باباتم😎", message_id)
                return 
            
            if text.strip() in ["شینا سازنده تو کیه"]:
                client.send_text(guid, "علیرضا باباعلی", message_id)
                return 
            if text.strip() in ["گنگ","گنگ بازی","گنگ بازیی"]:
            
                question = random.choice(n)
              
           
                client.send_video(guid, question, message_id)
                return
            if text.strip() in ["چشم"]:
                client.send_text(guid, "باریکلا😒", message_id)
                return 
            if text.strip() in ["دوست دارم"]:
                client.send_text(guid, "همینطور❤️🥂", message_id)
                return
            if text.strip() in ["فشار"]:
                client.send_text(guid, "نخور😒🥂", message_id)
                return
            if text.strip() in ["اینو ریمش کن","اینو بنش کن"]:
                client.send_text(guid, "تو نمیتونی هاع هاع😎🥂", message_id)
                return
            if text.strip() in ["دخترع","دختره","دختر هستی"]:
                client.send_text(guid, "اره مشکل داری😒🍑", message_id)
                return
            if text.strip() in ["تف","توف","بهت"]:
                client.send_text(guid, "تو صورتت😂👉", message_id)
                return
            if text.strip() in ["تو کی"]:
                client.send_text(guid, "من صدامم😂", message_id)
                return
            if text.strip() in ["بدم"]:
                client.send_text(guid, "جانم بده بزنیم🍑🥂😎", message_id)
                return
            if text.strip() in ["بدو"]:
                client.send_text(guid, "کجا بدوعم 🤨", message_id)
                return
            if text.strip() in ["برو","برم","بری"]:
                client.send_text(guid, "کجا؟/:🤨", message_id)
                return
            if text.strip() in ["گروه"]:
                client.send_text(guid, "هاع🤨🍑", message_id)
                return
            if text.strip() in ["ارع","ار","یس","اری"]:
                client.send_text(guid, "اینجا باکلاس بازی نداریم بگی اره تمام😎😂🥂🍑", message_id)
                return
            if text.strip() in [ "خبی","عالی","خفن","گاد","عالیی","عالی سید","افرین"]:
                media_url = "عالی (2).mp4"
                client.send_video(guid, media_url, message_id)
                return
            if text.strip() in ["علیرضا","علیرضا باباعلی","علیرضا کیست","باباعلی کیست","علیرضا باباعلی کیست","علیرضا باباعلی کیه","باباعلی کیه","علیرضا کیه","علیرضاباباعلی","علیرضا باباعلی کیست؟"]:
                client.send_text(guid, "سازنده ی منه ها🥂😎❤️", message_id)
                return
            if text.strip() in ["رباتی؟","رباته؟","رباته","رباتی"]:
                client.send_text(guid, "معلومه که رباتم مگر کوری😒🥂🍑", message_id)
                return
            if text.strip() in ["خب؟","خب","خو","خ"]:
                client.send_text(guid, "خب به جمالت😒", message_id)
                return
            if text.strip() in ["باخ","باع","بع","با"]:
                client.send_text(guid, "بع چیه؟😒🥂🍑", message_id)
                return
            if text.strip() in ["من هم","من"]:
                client.send_text(guid, "اره😎😒🍑", message_id)
                return
            if text.strip() in ["بد","چون"]:
                client.send_text(guid, "چی میگی اس**ل🍑", message_id)
                return
            if text.strip() in ["بنازم","به"]:
                client.send_text(guid, "خوشت اومد", message_id)
                return
            if text.strip() in ["خیلی","زیاد"]:
                client.send_text(guid, "دوست داری 😂🍑", message_id)
                return
            
            if text.strip() in [ "کالاف","کالاف دیوتی","کالاف بازان","کالاف"]:
                question = random.choice(z)
                client.send_image(guid, question, message_id)
                return
            if text.strip() in [ "والپیپر خفن","پس زمینه","والپیر","والپیپر"]:
                question = random.choice(u)
                client.send_image(guid, question, message_id)
                return
            if text.strip() in [ "دوست دارم","دوستت دارم","شینا دوست دارم","ربات دوست دارم"]:
                question = random.choice(v)
                client.send_gif(guid, question, message_id)
                return
            if text.strip() in [ "تکنولوژی","تکنولوژیا"]:
                question = "VID_20250212_222623_557.mp4"
                client.send_video(guid, question, message_id)
                return
            if text.strip() in [ "من قهر","من قهرم","من قهلم","قهرم","قهل","قهر"]:
                question = "download (5).jpg"
                client.send_image(guid, question, message_id)
                return
            if text.strip() in ["ربات رایگان میخوام","ربات میخوم","منم ربات میخوام","ربات رایگان میدی","ربات رایگان","رایگان"]:
                media_url = "images (5).jpg5"
                client.send_image(guid, media_url, message_id)
                return
            if text.strip() in ["کوروش","کوروش بزرگ","قط کوروش","هخامنش","هخامنشیان"]:
                media_url = "images (5).jpg5"
                client.send_video(guid, media_url, message_id)
                return
            if text.strip() in ["موزیک کوروش","کوروش","کوروش بزرگ","فقط کوروش","هخامنش","هخامنشیان"]:
                client.send_text(guid, "این کار ممکن است بین 5 تا 20 ثانیه طول بکشد منتظر باشید❤️🥂😎",message_id )
                media_url = "Manam Koorosh Padeshahe (320).mp3"
                client.send_music(guid, media_url, message_id)
                return
            if text.strip() in ["باش","باشه"]:
                client.send_text(guid, " باریکلا😒🥂 ", message_id)
                return
            if text.strip() in ["."," "]:
                client.send_text(guid, " چی زدی سلطان😂 ", message_id)
                return
            if text.strip() in ["تولد","تول منه","تولدم","تولدمه","تولته","تولدت","تنهام","تنها"]:
               
                media_url = "iqylvsycmnnynlroyitzozwabcwafwuokolyodbphnewesrfqgehxkqaoahlnxcf.mp4"
                client.send_video(guid, media_url, message_id)
                return
            if text.strip() in ["دلم","گرفته","دلم گرفته","تنهام","تنهای تنها","لات","لاتما","لاتی","بحث نکنید","نبود","بحث نکن","بحث"]:
               
                media_url = "tizbzyevrnscmsbttlnealseydgzbwlafbgmkoxyfuumatnxxqdkwruxnfbownez.mp4"
                client.send_video(guid, media_url, message_id)
                return
            if text.strip() in ["باوا","باع","باواع"]:
                client.send_text(guid, " درست صحبت کن لالی😒 ", message_id)
                return
            if text.strip() in ["فشاری","فشار","فشار خوردم","مشکل دای","مشکل","با من مشکل داری","فشار بخور"]:
               
                media_url = "patrick-s-gif(4).gif"
                client.send_gif(guid, media_url, message_id)
                return
            if text.strip() in ["چاکرم","نوکرم","فدات","دمت","دمت گرم"]:
                client.send_text(guid, "بس کن دیگه گرگعلی ", message_id)
                return
            if text.strip() in [ "پروفایل","پروفایل میخوام","پروف","پروفایل بده","درخواست پروفایل"]:
                question = random.choice(c)
                client.send_image(guid, question, message_id)
                return
            if text.strip() in [ "بیو","بیوگرافی","بیوگرافی میخوام","بیوگرافی بده","بیوگرافی میخوام"]:
                question = random.choice(f)
                client.send_text(guid, question, message_id)
                return
            
            if x.status_code == 200:

                         sup = BeautifulSoup(x.text, features= 'html.parser')
                         span = sup.find( name= 'span', attrs={'data-col': 'info.last_trade.PDrCotVal'})
            if span:
             print("طلا اینقدره", span.text)
            if text.strip() in ["قیمت طلا","طلا","قیمت طلا چنده"]:
                client.send_text(guid, span.text, message_id)
                return
            if v.status_code == 200:

                         s = BeautifulSoup(v.text, features= 'html.parser')
                         sp = s.find( name= 'span', attrs={'data-col': 'info.last_trade.PDrCotVal'})
            if sp:
             print("دلار اینقده", sp.text)
            if text.strip() in ["دلار","قیمت دلار","دلار چنده"]:
                client.send_text(guid,sp.text, message_id)
                return
            if g.status_code == 200:

                         h = BeautifulSoup(g.text, features= 'html.parser')
                         f = h.find( name= 'span', attrs={'data-col': 'info.last_trade.PDrCotVal'})
            if f:
             print("بیت کوین اینقدره", f.text)
            if text.strip() in ["بیتکوین","قیمت بیت کوین","بیت کوین"]:
                client.send_text(guid,f.text, message_id)
                return
            if findall("http", message.text):
                client.send_text(guid,"لینک نفرست دفعه ی بعدی ریم هستی😎😒لینکتو پاک میکنم ",message_id)
                message.delete()                        
            elif findall("@", message.text):
                 client.send_text(guid," لینک نفرست دفعه ی بعدی ریم هستی😎😒لینکتو پاک میکنم به من میگن ربات",message_id)
                 message.delete()
            if findall("از طریق لینک",message.text):
                client.send_gif(guid,"خوش اومدین.gif",message_id)
                message.reply("        خوش اومدی عزیزم❤️🥂          لطفا تبلیغ نکن چون خودم ریمت میکنم                   و تبلیغ رو پاک میکنم                    فحش بدی پاکش میکنم وریم میشی                                      دیگه هرکار خواستی بکن ازادی ❤️")
            if findall("ترک کرد",message.text):
                client.send_gif(guid,"60316488-7498-l__6528.webp",message_id)
                client.send_text(guid,"رفتی به درک هیچ ارزشی هم برای گروه نداشتی😎",message_id)
            if findall("کیر", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("کیرم", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("عنم", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("عن", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("کص", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("کس", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("پورن", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("سوپر", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("ننت", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("جنده", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("مادرت", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("ننتو", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("مادرتو", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("گایید", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("گاییدم", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("میگام", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("میگامت", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("خارتو", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")
            if findall("خوارتو", message.text):
                client.send_text(guid,"فحش نده ریم میشی😡",message_id)
                message.delete("konni")

            


        except Exception as e:
            print(f"خطای نامشخص در پردازش پیام: {e}")
           

    while True:
        try:
            print("ربات شروع به کار کرد...")
            client.run()
        except Exception as e:
            print(f"خطای اجرای ربات: {e}")
            print("ربات مجدداً شروع به کار می‌کند...")
            time.sleep(5)
          
# اجرای ربات


if __name__ == "__main__":
    run_bot()