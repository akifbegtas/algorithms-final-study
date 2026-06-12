# -*- coding: utf-8 -*-
# Düzeltilmiş L1-L5: OMNeT++ (L1-L3), Greedy (L4), Big O (L5)

NEW = []

# ===========================================================================
# L1 — OMNeT++ ve TicToc'a Giriş (Discrete Event Simulation)
# ===========================================================================
NEW.append({
"code": "L1",
"title": "OMNeT++ ve TicToc'a Giriş (DES)",
"subtitle": "Discrete Event Simulation, modüller, mesajlaşma, .ned/.cc/.ini, yaşam döngüsü",
"body": r"""
## Discrete Event Simulation (DES) nedir?
**DES (Ayrık Olay Simülasyonu)**, değişikliklerin **sürekli değil, belirli zaman noktalarında
(olaylarda)** olduğu sistemleri modelleyip analiz eden bir tekniktir. Sistem yalnızca bir **olay
(event)** gerçekleştiğinde durum değiştirir.

**Örnekler:**
- **Bilgisayar ağı:** olaylar = paket varışı, router yönlendirmesi, link arızası.
- **Trafik ağı:** olaylar = araç varışı, şerit değişimi, ışık değişimi.
- **Üretim hattı:** olaylar = hammadde varışı, makine arızası, ürün tamamlanması.
- **Hastane acil:** olaylar = hasta varışı, doktor ataması, tedavi bitişi.

**Faydaları:** risksiz deney (gerçek sisteme zarar vermeden senaryo test etme), daha iyi karar,
düşük maliyet (fiziksel prototipten ucuz), ölçeklenebilirlik. Sürekli süreçler (sıvı akışı, sıcaklık)
için ise **continuous simulation** gerekir.

## OMNeT++ nedir?
**OMNeT++**, sistemleri **modül (module)** denen bileşenlerle modelleyen bir **discrete event
simulation framework**'üdür. Modüller birbirleriyle **mesaj geçişi (message passing)** ile
haberleşir. Ağ, protokol vb. modellemede kullanılır.

## TicToc projesi
OMNeT++'ın temel öğretici örneğidir: **iki modül — `tic` ve `toc`** — bir mesajı birbirine
gönderir. `tic`, `toc`'a `"tictocMsg"` gönderir; `toc` mesajı geri gönderir. Gösterdiği kavramlar:
modül oluşturma, **mesaj geçişi**, **olay zamanlama (event scheduling)**.

## Bir OMNeT++ projesinin 3 temel dosyası
- **`.ned`** (Network Description): ağ ve modül yapısını, kapıları (gate) ve bağlantıları tanımlar.
- **`.cc` / `.h`**: modül davranışını (C++) uygular.
- **`.ini`** (`omnetpp.ini`): simülasyonun çalışma-zamanı parametrelerini yapılandırır.

### NED dosyası (yapı)
```text
simple Txc1 {
    gates:
        input in;       // giriş kapısı
        output out;      // çıkış kapısı
}
network Tictoc1 {
    submodules:
        tic: Txc1;
        toc: Txc1;
    connections:
        tic.out --> {  delay = 100ms; } --> toc.in;
        tic.in  <-- {  delay = 100ms; } <-- toc.out;
}
```

### C++ modül davranışı (Txc1)
```cpp
#include <string.h>
#include <omnetpp.h>
using namespace omnetpp;

class Txc1 : public cSimpleModule {
  protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};
Define_Module(Txc1);

void Txc1::initialize() {
    // Sadece "tic" ilk mesajı başlatır
    if (strcmp("tic", getName()) == 0) {
        cMessage *msg = new cMessage("tictocMsg");
        send(msg, "out");          // mesajı 'out' kapısından gönder
    }
}

void Txc1::handleMessage(cMessage *msg) {
    send(msg, "out");              // gelen mesajı geri yolla (ping-pong)
}
```

### omnetpp.ini
```text
[General]
network = Tictoc1
```

## Modül yaşam döngüsü fonksiyonları
- **`initialize()`** — simülasyon başında bir kez çağrılır (başlangıç ayarları).
- **`handleMessage(cMessage *msg)`** — modüle bir mesaj geldiğinde çağrılır (ana mantık burada).
- **`activity()`** — alternatif modül davranış fonksiyonu (coroutine tarzı).
- **`finish()`** — simülasyon bittiğinde çağrılır (istatistik kaydı).

## Mesaj yönetimi fonksiyonları
- **`send(msg, "gateName")`** — mesajı bir **kapıdan başka modüle** gönderir.
- **`scheduleAt(t, msg)`** — gelecekte `t` anında modülün **kendine** mesaj planlar (self-message).
- **`cancelEvent(msg)`** — planlanmış bir mesajı iptal eder.

:::exam Sık çıkanlar: DES tanımı; OMNeT++ modüllerinin mesajla haberleşmesi; .ned/.cc/.ini
görevleri; initialize() vs handleMessage() vs finish(); send() ile scheduleAt() farkı.
:::
""",
"qa": [
 ("Discrete Event Simulation (DES) nedir ve neyi modeller?",
  "**DES (Ayrık Olay Simülasyonu)**, sistemdeki değişikliklerin **sürekli değil, belirli zaman noktalarında — yani olaylarda (events)** gerçekleştiği sistemleri modelleyip analiz eden bir tekniktir. Sistem yalnızca bir olay olduğunda durum değiştirir (örn. paket varışı, hasta gelişi). Sürekli değişen süreçler (sıvı akışı, sıcaklık) için DES yerine **continuous simulation** kullanılır."),
 ("OMNeT++ nedir ve modülleri birbiriyle nasıl haberleşir?",
  "**OMNeT++**, bir **discrete event simulation framework**'üdür; kütüphaneler, araçlar ve API'lerle sistem simülasyonu kurmayı sağlar. Sistemler **modül (module)** denen bileşenlerle modellenir ve bu modüller birbirleriyle **mesaj geçişi (message passing)** yoluyla haberleşir. Özellikle iletişim ağları ve protokollerin modellenmesinde kullanılır."),
 ("TicToc projesinde `tic` ve `toc` modülleri ne yapar?",
  "TicToc, OMNeT++'ın temel öğreticisidir: **iki modül, `tic` ve `toc`**, bir mesajı birbirine gönderir. `tic` başlangıçta `\"tictocMsg\"` adlı mesajı oluşturup `toc`'a yollar; `toc` aldığı mesajı geri `tic`'e gönderir ve bu **ping-pong** sürer. Amaç; modül oluşturma, **mesaj geçişi** ve **olay zamanlama** kavramlarını göstermektir."),
 ("Bir OMNeT++ projesindeki `.ned`, `.cc/.h` ve `.ini` dosyalarının görevleri nedir?",
  "**`.ned` (Network Description):** ağın ve modüllerin **yapısını** — kapıları (gate) ve bağlantıları — tanımlar. **`.cc`/`.h`:** modülün **davranışını** C++ ile uygular (initialize, handleMessage vb.). **`.ini` (omnetpp.ini):** simülasyonun **çalışma-zamanı yapılandırmasıdır** — hangi network çalışacak, parametre değerleri vb. Yani sırasıyla: yapı, davranış, yapılandırma."),
 ("`initialize()` ve `handleMessage()` fonksiyonları ne zaman çağrılır?",
  "**`initialize()`** simülasyonun **başında bir kez** çağrılır; başlangıç değerleri ve (TicToc'ta) ilk mesajın gönderilmesi burada yapılır. **`handleMessage(cMessage *msg)`** ise modüle **her mesaj geldiğinde** çağrılır ve modülün ana çalışma mantığını içerir. Ayrıca simülasyon sonunda bir kez **`finish()`** çağrılır (istatistik kaydı için)."),
 ("`send()` ile `scheduleAt()` arasındaki fark nedir?",
  "**`send(msg, \"gateName\")`** bir mesajı belirtilen **kapıdan başka bir modüle** yollar — modüller arası iletişim içindir. **`scheduleAt(t, msg)`** ise mesajı **modülün kendisine**, gelecekteki `t` anında teslim edilmek üzere planlar (**self-message**); zamanlayıcı/gecikme modellemek için kullanılır. Kısaca: `send` dışarı gönderir, `scheduleAt` kendine zamanlar. Planlanan bir self-message `cancelEvent(msg)` ile iptal edilebilir."),
 ("Aşağıdaki `handleMessage` ne yapar?\n\n```cpp\nvoid Txc1::handleMessage(cMessage *msg) {\n    send(msg, \"out\");\n}\n```",
  "Bu fonksiyon, modüle gelen **her mesajı olduğu gibi `out` kapısından geri gönderir**. TicToc'ta bu, `tic` ve `toc` arasında mesajın sonsuza dek **ileri-geri (ping-pong)** gitmesini sağlar — mesaj hiç silinmediği ve bir sayaçla durdurulmadığı için simülasyon kendiliğinden bitmez. (Sonraki derste `counter` ile durdurma eklenir.)"),
]
})

# ===========================================================================
# L2 — TicToc İyileştirmeleri (Part 3)
# ===========================================================================
NEW.append({
"code": "L2",
"title": "TicToc İyileştirmeleri — OMNeT++ (Part 3)",
"subtitle": "Icon, logging (EV), state variable (counter), WATCH, processing delay, timer",
"body": r"""
İki düğümlü TicToc simülasyonunu **görsel ve davranışsal** olarak iyileştiririz. Başlıklar:
ikon ekleme, loglama, durum değişkenleri, parametreler, NED kalıtımı, işlem gecikmesi, rastgele
sayılar, timeout/timer iptali, yeniden iletim.

## 3.1 İkon ve renk ekleme (NED)
Modüllere GUI'de ikon/renk vermek için NED'de **display string** (`i=` tag) kullanılır.
```text
simple Txc {
    parameters:
        @display("i=block/routing");   // ikon
    gates:
        input in;
        output out;
}
// Ağ tanımında renk:
//   tic: Txc { @display("i=,cyan"); }
//   toc: Txc { @display("i=,gold"); }
```

## 3.2 Loglama — EV makrosu
Modülün ne yaptığını yazdırmak için OMNeT++'ın **`EV`** log akışı kullanılır (`cout` gibi).
```cpp
EV << "Mesaj gonderiliyor: " << msg->getName() << "\n";
```
Loglar runtime log penceresinde görünür; modül başına ayrı log penceresi açılabilir.

## 3.3 Durum değişkeni (state variable) + simülasyonu durdurma
Mesaj alışverişini saymak için bir **counter** sınıf üyesi eklenir; `initialize()`'da değer verilir
(örn. 10), `handleMessage()`'da her mesajda azaltılır, **sıfıra inince mesaj silinir** ve
simülasyon (o akış için) biter. **`WATCH(counter)`** counter'ı GUI inspector'da görünür yapar.
```cpp
class Txc : public cSimpleModule {
  private:
    int counter;                       // durum değişkeni
  protected:
    virtual void initialize() override;
    virtual void handleMessage(cMessage *msg) override;
};
Define_Module(Txc);

void Txc::initialize() {
    counter = 10;                      // başlangıç değeri
    WATCH(counter);                    // GUI'de izlenebilir yap
    if (strcmp("tic", getName()) == 0)
        scheduleAt(0.0, new cMessage("tictocMsg"));
}

void Txc::handleMessage(cMessage *msg) {
    counter--;                                  // her mesajda azalt
    if (counter == 0) {
        EV << getName() << ": counter bitti, mesaj siliniyor.\n";
        delete msg;                             // akış durur
    } else {
        EV << "counter = " << counter << ", mesaj geri gonderiliyor.\n";
        send(msg, "out");
    }
}
```

## 3.6 İşlem gecikmesi (processing delay) — self-message
Bir modülün mesajı hemen değil, bir **gecikmeyle** işlemesi için **self-message** (kendine mesaj)
kullanılır: dış mesaj gelince saklanır ve `scheduleAt` ile bir timer planlanır; timer ateşlenince
mesaj gönderilir.
```cpp
void Txc::handleMessage(cMessage *msg) {
    if (msg == event) {                         // self-message (timer) geldi
        send(message, "out");                   // bekleyen mesajı gönder
        message = nullptr;
    } else {                                    // dışarıdan mesaj geldi
        message = msg;                          // sakla
        scheduleAt(simTime() + delayTime, event);  // gecikme sonrası işle
    }
}
```

## 3.8 Timeout ve timer iptali
Bir timeout (zaman aşımı) timer'ı `scheduleAt` ile kurulur; beklenen mesaj zamanında gelirse
timer **`cancelEvent(timeoutEvent)`** ile iptal edilir. Gelmezse mesaj **yeniden iletilir**
(retransmit). Rastgele kayıp/gecikme modellemek için `intuniform()`, `exponential()` gibi
**rastgele sayı** üreticileri ve `.ned` **parametreleri** kullanılır.

:::exam Bilinmesi gerekenler: EV ne işe yarar; counter ile simülasyonun durdurulması (counter==0
→ delete msg); WATCH() ne yapar; processing delay için self-message + scheduleAt; timer iptali
cancelEvent ile.
:::
""",
"qa": [
 ("OMNeT++'ta `EV` makrosu ne işe yarar?",
  "**`EV`**, OMNeT++'ın **loglama akışıdır**; tıpkı `cout` gibi `EV << \"...\"` şeklinde kullanılır ve modülün ne yaptığını **simülasyon log penceresine** yazdırır. Büyük modellerde log seviyeleri, kanalları ve filtreleme sunan gelişmiş bir loglama olanağının en basit hâlidir. Hata ayıklama ve mesaj akışını izleme için kullanılır."),
 ("TicToc'a bir state variable (counter) eklenince simülasyon nasıl durdurulur?",
  "Bir **`counter`** sınıf üyesi eklenir, `initialize()` içinde bir değere ayarlanır (örn. 10) ve **`handleMessage()` içinde her mesaj geldiğinde azaltılır**. Counter **sıfıra ulaştığında** modül mesajı geri göndermek yerine **`delete msg`** ile siler; böylece artık olay üretilmez ve o akış için simülasyon **kendiliğinden durur**. (Mesaj silinmezse ping-pong sonsuza dek sürer.)"),
 ("`WATCH(counter)` ifadesi ne yapar?",
  "**`WATCH(counter)`**, `counter` değişkenini OMNeT++ **GUI (Qtenv) inspector**'ında **görünür/izlenebilir** kılar. Genellikle `initialize()` içinde çağrılır. Simülasyon çalışırken modüle tıklayıp counter'ın anlık değerini görmeyi sağlar; davranışı izlemek ve hata ayıklamak için kullanışlıdır. Çalışma mantığını değiştirmez, sadece görünürlük katar."),
 ("OMNeT++'ta bir işlem gecikmesi (processing delay) nasıl modellenir?",
  "**Self-message (kendine mesaj)** ile modellenir. Dışarıdan bir mesaj geldiğinde hemen göndermek yerine mesaj saklanır ve **`scheduleAt(simTime() + delayTime, event)`** ile bir timer planlanır. Bu self-message (`event`) ateşlendiğinde `handleMessage` tekrar çağrılır; `msg == event` kontrolüyle anlaşılır ve bekletilen mesaj o anda gönderilir. Böylece mesaj `delayTime` kadar gecikmeyle işlenmiş olur."),
 ("Modüllere GUI'de ikon ve renk nasıl verilir?",
  "NED dosyasında **display string** (`@display(\"...\")`, eski gösterimle `i=` tag) kullanılır. Örn. `@display(\"i=block/routing\")` modüle yönlendirme ikonu verir; ağ tanımında `@display(\"i=,cyan\")` ve `@display(\"i=,gold\")` ile `tic` cyan, `toc` sarı renklendirilir. Bu değişiklikler tamamen **NED dosyasında** yapılır ve simülasyonu görsel olarak ayırt etmeyi kolaylaştırır (davranışı etkilemez)."),
 ("Bir timeout timer'ı nasıl kurulur ve nasıl iptal edilir?",
  "Bir timeout, **`scheduleAt(simTime() + timeout, timeoutEvent)`** ile bir self-message planlanarak kurulur. Beklenen mesaj/onay **zamanında gelirse** timer'a artık gerek yoktur ve **`cancelEvent(timeoutEvent)`** ile iptal edilir. Mesaj gelmez ve timeout ateşlenirse, modül mesajı **yeniden iletir (retransmit)**. Bu, güvenilir iletim (stop-and-wait) protokollerinin temel mantığıdır."),
 ("Self-message (kendine mesaj) nedir ve normal mesajdan farkı nedir?",
  "**Self-message**, bir modülün **`scheduleAt` ile kendi kendisine** gelecekteki bir an için planladığı mesajdır; başka bir modüle gitmez, zamanlayıcı/timer veya gecikme görevi görür. **Normal mesaj** ise `send()` ile bir **kapıdan başka bir modüle** gönderilir. `handleMessage` içinde gelen mesajın self-message olup olmadığı genelde `msg->isSelfMessage()` veya `msg == event` ile ayırt edilir."),
]
})

# ===========================================================================
# L3 — Part 4: Gerçek Ağ (TicToc10-15)
# ===========================================================================
NEW.append({
"code": "L3",
"title": "TicToc'u Gerçek Ağa Dönüştürmek — OMNeT++ (Part 4-5)",
"subtitle": "Çok düğüm, channel, two-way bağlantı, özel mesaj sınıfı, istatistik (finish/recordScalar)",
"body": r"""
Bu derste 2-düğümlü TicToc, **çok düğümlü gerçek bir ağa** dönüştürülür ve istatistik toplama
eklenir.

## TicToc10: İkiden çok düğüm
Modül bir **dizi (vector)** hâline getirilir (`tic[6]` gibi) ve düğümler birbirine bağlanır. Mesaj
artık doğrudan değil, **hedefe doğru yönlendirilerek (routing)** iletilir. Bir düğüm mesajı
aldığında **kendisi hedef mi** diye bakar; değilse **rastgele bir komşuya** iletir.

```cpp
void Txc::handleMessage(cMessage *msg) {
    if (getIndex() == 3) {                 // 3. düğüm hedef olsun
        EV << "Mesaj hedefe ulasti.\n";
        delete msg;
    } else {
        int n = gateSize("gate");          // komşu/kapı sayısı
        int k = intuniform(0, n - 1);      // rastgele bir kapı seç
        EV << "Mesaj " << k << ". kapidan iletiliyor.\n";
        send(msg, "gate$o", k);            // forward (ilet)
    }
}
```

## TicToc11: Channel (kanal) ve inner type definitions
Tekrarlayan bağlantı özellikleri (gecikme, veri hızı) için NED içinde **`types`** bölümünde bir
**channel** tanımlanır ve tüm bağlantılarda kullanılır.
```text
network Tictoc11 {
    types:
        channel Channel extends ned.DelayChannel {
            delay = 100ms;
        }
    submodules:
        tic[6]: Txc;
    connections:
        tic[0].gate++ <--> Channel <--> tic[1].gate++;
        // ...
}
```

## TicToc12: İki yönlü (two-way) bağlantılar
Ayrı `in`/`out` kapıları yerine **`inout gate`** kullanılır; bağlantılar `<-->` ile çift yönlü
kurulur. Bu, kod ve NED'i sadeleştirir.

## TicToc13: Özel mesaj sınıfı (.msg)
Mesaja ek alanlar (kaynak, hedef, hop sayısı) koymak için bir **mesaj sınıfı** `.msg` dosyasında
tanımlanır; OMNeT++ bundan C++ sınıfı üretir.
```text
// tictoc13.msg
message TicTocMsg {
    int source;
    int destination;
    int hopCount = 0;
}
```
Gelen bir `cMessage*`'ı bu türe **güvenli** çevirmek için **`check_and_cast<>()`** kullanılır
(başarısızsa hata verir):
```cpp
TicTocMsg *ttmsg = check_and_cast<TicTocMsg *>(msg);
if (ttmsg->getDestination() == getIndex()) {
    EV << "Ulasti! hop = " << ttmsg->getHopCount() << "\n";
    delete ttmsg;
} else {
    ttmsg->setHopCount(ttmsg->getHopCount() + 1);   // hop say
    forwardMessage(ttmsg);
}
```

## Part 5 — İstatistik toplama
- **`refreshDisplay()`**: GUI'nin (Qtenv) modülün **görsel temsilini** güncellemek için çağırdığı
  özel fonksiyondur (sayaç gösterimi vb. buraya yazılır).
- **`finish()`**: simülasyon **bittiğinde otomatik** çağrılan yaşam-döngüsü fonksiyonudur.
- **`recordScalar(name, value)`**: tek bir sayısal (scalar) değeri sonuç dosyasına kaydeder.
```cpp
void Txc::finish() {
    recordScalar("#sent", numSent);          // gönderilen paket sayısı
    recordScalar("#received", numReceived);  // alınan paket sayısı
}
```

:::exam Sık sorulanlar: çok düğümde rastgele yönlendirme (intuniform + send forward); channel'ın
types bölümünde tanımı; inout/two-way bağlantı; .msg ile özel mesaj; check_and_cast<>() güvenli
dönüşüm; finish() + recordScalar() ile istatistik.
:::
""",
"qa": [
 ("TicToc ikiden çok düğüme çıkarıldığında mesaj nasıl iletilir?",
  "Modül bir **dizi (vector, örn. `tic[6]`)** hâline getirilir ve düğümler birbirine bağlanır. Bir düğüm mesajı aldığında önce **kendisinin hedef olup olmadığına** bakar (`getIndex()` ile). Hedef değilse mesajı **bir komşuya iletir (forward)** — temel TicToc'ta hedef bulunana kadar **`intuniform(0, n-1)` ile rastgele seçilen** bir kapıdan gönderilir. Hedefe ulaşınca mesaj silinir."),
 ("OMNeT++'ta channel (kanal) nedir ve neden `types` bölümünde tanımlanır?",
  "**Channel (kanal)**, bir bağlantının **gecikme (delay)**, **veri hızı (datarate)**, **bit hata oranı** gibi özelliklerini taşıyan bir tiptir. Aynı özellikler birçok bağlantıda tekrar edeceği için, channel NED'de **`types` bölümünde bir kez tanımlanır** (örn. `Channel extends ned.DelayChannel { delay = 100ms; }`) ve tüm bağlantılarda yeniden kullanılır. Bu, kod tekrarını önler ve bakımı kolaylaştırır."),
 ("İki yönlü (two-way / inout) bağlantı nedir, ne avantaj sağlar?",
  "Ayrı `input in` ve `output out` kapıları yerine tek bir **`inout gate`** tanımlanır ve bağlantılar **`<-->`** operatörüyle çift yönlü kurulur. Böylece her komşu için iki ayrı kapı/bağlantı yazmak yerine tek bir iki yönlü bağlantı kullanılır; bu da NED tanımını ve modül kodunu **sadeleştirir**, özellikle çok düğümlü ağlarda."),
 ("Neden özel bir mesaj sınıfı (.msg) tanımlanır?",
  "Temel `cMessage` yalnızca isim/tür taşır. Gerçek bir ağ protokolünde mesaja **ek bilgi** gerekir: **kaynak (source)**, **hedef (destination)**, **hop sayısı** vb. Bunları taşımak için `.msg` dosyasında bir **mesaj sınıfı** (örn. `TicTocMsg`) tanımlanır; OMNeT++ bundan otomatik olarak getter/setter'lı bir C++ sınıfı üretir. Böylece yönlendirme ve istatistik için gereken alanlar mesajla birlikte taşınır."),
 ("`check_and_cast<>()` ne işe yarar ve neden tercih edilir?",
  "**`check_and_cast<TicTocMsg*>(msg)`**, bir `cMessage*` işaretçisini istenen mesaj türüne **güvenli biçimde** dönüştürür. İçeride `dynamic_cast` dener; **dönüşüm başarısız olursa** (mesaj o tür değilse) sessizce `nullptr` döndürmek yerine **anlaşılır bir hata fırlatır**. Bu, yanlış türde mesaj geldiğinde hatayı erken ve net yakalamayı sağlar; çıplak cast'e göre çok daha güvenlidir."),
 ("`finish()` ve `recordScalar()` ne işe yarar?",
  "**`finish()`**, simülasyon **sona erdiğinde otomatik** çağrılan bir yaşam-döngüsü fonksiyonudur; genelde toplanan istatistikleri kaydetmek için kullanılır. **`recordScalar(name, value)`**, tek bir **sayısal (scalar) değeri** (örn. gönderilen paket sayısı) simülasyon **sonuç dosyasına** yazar. İkisi birlikte, koşu bitince `recordScalar(\"#sent\", numSent)` gibi özet metriklerin kaydedilmesini sağlar."),
 ("`refreshDisplay()` fonksiyonu ne zaman ve niçin çağrılır?",
  "**`refreshDisplay()`**, **Qtenv gibi grafik arayüzlerin**, olaylar işlendikten sonra ekranın güncellenmesi gerektiğinde tüm bileşenlerde çağırdığı özel bir fonksiyondur. Görselleştirmeyle ilgili kod (display string güncelleme, sayaç gösterimi, canvas figürleri) bu metodun içine taşınır. Böylece görsel güncelleme, simülasyon mantığından ayrılır ve yalnızca GUI'nin ihtiyaç duyduğunda verimli biçimde yapılır."),
]
})

# ===========================================================================
# L4 — Greedy Method
# ===========================================================================
NEW.append({
"code": "L4",
"title": "Greedy Method (Açgözlü Yöntem) ve Algoritma Tasarım Teknikleri",
"subtitle": "Problem çözme yöntemleri, feasible/optimal çözüm, optimizasyon, graf temelleri",
"body": r"""
## Bir problemi çözmenin farklı yöntemleri
Aynı problem farklı tasarım teknikleriyle çözülebilir:
- **Divide-and-Conquer (Böl-Yönet):** problemi **bağımsız** alt problemlere böler, özyinelemeli
  çözer, birleştirir (örn. Merge Sort O(n log n)).
- **Dynamic Programming (DP):** **örtüşen (overlapping)** alt problemleri böler, **memoization**
  ile tekrarı önler (örn. Fibonacci O(n), shortest path, knapsack).
- **Greedy (Açgözlü):** her adımda **yerel (locally) optimal** seçimi yaparak global optimuma
  ulaşmayı umar (örn. Huffman Coding O(n log n)).
- **Brute Force / Exhaustive Search:** **tüm** olası çözümleri dener (üstel zaman, büyük girdide
  verimsiz).

## Greedy Method nedir?
Greedy yöntemi, çözümü adım adım kurar ve **her adımda o an en iyi görünen (locally optimal)
seçeneği** alır; bu seçimleri geri almaz. Amaç bu yerel seçimlerin **global optimuma** götürmesidir.
Greedy, **optimizasyon problemlerini** çözmek için kullanılır.

### Temel kavramlar (Sakarya → İstanbul, 3 saatte örneği)
- **Kısıt (constraint):** "3 saatte" gibi sağlanması gereken koşul.
- **Feasible solution (uygun çözüm):** kısıtı **sağlayan** çözümler (örn. araba, tren, uçak).
  Yürümek/bisiklet 3 saate sığmaz → **infeasible (uygun değil)**.
- **Optimal solution (en iyi çözüm):** feasible çözümler arasından **en iyisi** (örn. minimum
  maliyet/süre) — genelde **tek**tir.
- **Optimization problem:** **maksimum** veya **minimum** sonuç isteyen problem; greedy tam da
  bunları çözer.

### Greedy genel yapısı (sözde kod)
```text
Greedy(C):                       // C = aday kümesi (candidate set)
    S = ∅                        // çözüm
    while C boş değil ve S çözüm değil:
        x = Select(C)            // locally optimal adayı seç
        C = C - {x}
        if Feasible(S ∪ {x}):    // uygunsa ekle
            S = S ∪ {x}
    if Solution(S): return S
    else: return "çözüm yok"
```
Adımlar: adayları **filtrele/sırala** (max veya min'e göre), **uygun (feasible)** olanları seç,
aralarından **en iyisini (optimal)** al.

:::warn Greedy her zaman global optimumu **garanti etmez** — sadece "umar". Bazı problemlerde
(örn. 0/1 Knapsack) greedy yanlış sonuç verir; orada DP gerekir. Fractional Knapsack, Huffman,
Dijkstra, Prim, Kruskal ise greedy ile **optimal** çözülür.
:::

## Graf temelleri (greedy/graf algoritmaları için)
Birçok greedy algoritması graf üzerinde çalışır:
- **Graph G = (V, E):** V düğümler (vertices), E kenarlar (edges). Kenar `(v, w)` iki düğümü bağlar.
- **Degree (derece):** bir düğüme değen kenar sayısı.
- **Path (yol):** bir düğümden diğerine giden kenar dizisi; **path length** = yoldaki kenar/düğüm sayısı.
- **Reachable / connected:** her düğüm her düğümden erişilebiliyorsa graf **bağlıdır (connected)**.
- **Weighted graph:** kenarların **ağırlığı (cost)** vardır; çoğu graf negatif ağırlığa izin vermez.
- **Directed graph (digraph):** kenarlar **tek yönlüdür**; düğümün ayrı **in/out degree**'si olur.

:::exam Sınavda: D&C/DP/Greedy/Brute force farkları; feasible vs optimal çözüm; optimization
problem tanımı; greedy'nin global optimumu garanti etmemesi; graf temel terimleri (V, E, degree,
directed, weighted).
:::
""",
"qa": [
 ("Greedy (açgözlü) method nedir ve nasıl çalışır?",
  "Greedy method, çözümü **adım adım** kuran ve her adımda **o an en iyi görünen — locally optimal — seçeneği** alıp bunu bir daha geri almayan bir algoritma tasarım tekniğidir. Bu yerel seçimlerin sonunda **global optimuma** ulaşmayı **umar**. Özellikle **optimizasyon problemlerini** (maksimum/minimum arayan) çözmek için kullanılır. Örnekler: Huffman coding, Dijkstra, Prim, Kruskal, fractional knapsack."),
 ("Feasible solution (uygun çözüm) ile optimal solution (en iyi çözüm) arasındaki fark nedir?",
  "**Feasible solution**, problemin **kısıtını sağlayan** herhangi bir çözümdür (örn. 'Sakarya→İstanbul 3 saatte' kısıtını araba, tren ve uçak sağlar; yürümek sağlamaz → infeasible). **Optimal solution** ise feasible çözümler arasından **belirli bir ölçüte göre en iyisidir** (örn. en düşük maliyet veya en kısa süre) ve genelde tektir. Yani önce uygun olanlar süzülür, sonra aralarından en iyisi seçilir."),
 ("Optimization problem (optimizasyon problemi) nedir? Greedy ne tür problemleri çözer?",
  "**Optimization problem**, **maksimum** ya da **minimum** bir sonuç isteyen problemdir (en düşük maliyet, en yüksek değer, en kısa yol vb.). **Greedy method**, tam olarak bu tür **optimizasyon problemlerini** çözmek için kullanılır: her adımda yerel olarak en iyi (max/min) seçeneği alarak optimal sonuca ulaşmaya çalışır."),
 ("Divide-and-Conquer, Dynamic Programming, Greedy ve Brute Force arasındaki temel farklar nelerdir?",
  "**Divide-and-Conquer:** problemi **bağımsız** alt problemlere böler, özyinelemeli çözüp birleştirir (Merge Sort). **Dynamic Programming:** **örtüşen** alt problemleri **memoization** ile tekrar hesaplamadan çözer (Fibonacci, knapsack). **Greedy:** her adımda **yerel optimal** seçimi yapar (Huffman). **Brute Force:** **tüm** olası çözümleri dener — kesin ama üstel zaman, büyük girdide verimsiz."),
 ("Greedy method her zaman global optimal çözümü garanti eder mi?",
  "**Hayır.** Greedy yalnızca her adımda yerel en iyiyi seçer ve global optimuma ulaşmayı **umar** — garanti etmez. Bazı problemlerde greedy doğru sonucu verir (Fractional Knapsack, Huffman, Dijkstra, Prim, Kruskal), bazılarında ise **başarısız olur**; klasik örnek **0/1 Knapsack**'tir; orada en yoğun nesneyi seçmek optimumu kaçırabilir ve **Dynamic Programming** gerekir. Greedy'nin doğruluğu probleme özeldir."),
 ("Greedy yöntemiyle optimal olarak çözülebilen algoritmalardan örnekler verin.",
  "Greedy ile **optimal** çözülen klasik algoritmalar: **Huffman Coding** (O(n log n)), **Dijkstra** (en kısa yol, negatif olmayan ağırlıklarda), **Prim** ve **Kruskal** (minimum spanning tree), **Fractional Knapsack** (value/weight oranına göre). Bu problemlerde 'greedy choice property' ve 'optimal substructure' özellikleri sağlandığı için yerel seçimler global optimuma götürür."),
 ("Graf temel terimlerini açıklayın: G=(V,E), degree, weighted graph, directed graph.",
  "**G = (V, E):** graf, düğümler kümesi **V** (vertices) ve kenarlar kümesi **E** (edges) ile tanımlanır; kenar `(v, w)` iki düğümü bağlar. **Degree (derece):** bir düğüme değen kenar sayısı. **Weighted graph:** kenarların bir **ağırlığı/maliyeti** olan graf (çoğu negatif ağırlığa izin vermez). **Directed graph (digraph):** kenarların **tek yönlü** olduğu graf; burada her düğümün ayrı **in-degree** ve **out-degree**'si vardır."),
]
})

# ===========================================================================
# L5 — Big O notation
# ===========================================================================
NEW.append({
"code": "L5",
"title": "Big O Notasyonu",
"subtitle": "Karmaşıklık, Big O hesaplama, sadeleştirme, growth functions, O/Ω/Θ, graf algoritmaları tablosu",
"body": r"""
## Big O nedir?
**Big O notasyonu**, bir algoritmanın **verimliliğini** — girdi boyutu büyüdükçe nasıl
davrandığını — tanımlayan standart bir yöntemdir. Ölçeklenebilir ve verimli yazılım tasarımı için
kritiktir. **Algoritma karmaşıklığı**, bir algoritmanın bir problemi çözmek için harcadığı
**zaman ve/veya bellek** miktarının, girdi boyutunun bir fonksiyonu olarak ölçüsüdür.

## Big O nasıl hesaplanır?
1. Performansı etkileyen **girdi boyutunu (n)** belirle.
2. Zaman karmaşıklığına katkı veren **temel işlemleri (basic operations) say**.
3. İşlemlerin n ile nasıl büyüdüğünü **n cinsinden bir fonksiyon** olarak ifade et.
4. **Sadeleştir:**
   - **Sabitleri at:** `O(2n) → O(n)`.
   - **Sadece en yüksek dereceli terimi tut:** `O(n² + n) → O(n²)`.

```cpp
// O(2n) -> O(n): sabit katsayı atılır
for (int i = 0; i < n; i++) { x++; y++; }     // ~2n işlem  =>  O(n)

// O(n^2 + n) -> O(n^2): en yüksek dereceli terim kalır
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) x++;          // n^2
for (int i = 0; i < n; i++) x++;              // + n   =>  O(n^2)
```

## Büyüme fonksiyonları (growth functions)
Girdi büyüdükçe büyüme hızları (küçükten büyüğe):
`O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)`

| n | 1 | log n | n | n log n | n² | n³ | 2ⁿ |
|---|---|---|---|---|---|---|---|
| 10 | 1 | ~3 | 10 | ~33 | 100 | 1.000 | ~1.0e3 |
| 20 | 1 | ~4 | 20 | ~86 | 400 | 8.000 | ~1.0e6 |
| 40 | 1 | ~5 | 40 | ~213 | 1.600 | 64.000 | ~1.1e12 |

## Big O — graf algoritmaları tablosu (sınavda çok işine yarar)
| Algoritma | Big O |
|---|---|
| Breadth-First Search (BFS) | O(V + E) |
| Depth-First Search (DFS) | O(V + E) |
| Dijkstra | O(V²) (yoğun) veya O(E log V) (seyrek) |
| Bellman-Ford | O(V·E) |
| Floyd-Warshall | O(V³) |
| Prim (MST) | O(E log V) |
| Kruskal (MST) | O(E log V) |
| Topological Sort | O(V + E) |

## Üç asimptotik sınır: Big O, Big Ω, Big Θ
- **Big O** → algoritmanın **worst case** (en kötü durum) zamanı; ifadeden **daha yavaş ya da
  aynı hızda** büyüyen fonksiyonlar kümesi (üst sınır).
- **Big Ω** → **best case** (en iyi durum); ifadeden **daha hızlı ya da aynı hızda** büyüyenler
  (alt sınır).
- **Big Θ** → **average case**; fonksiyon hem O(ifade) hem Ω(ifade) içindeyse, yani alttan ve
  üstten aynı oranla sınırlıysa Θ kullanılır (sıkı sınır).

:::tip Matematikte gerçel değişken için `x` ve `f(x), g(x)` kullanılır; algoritmalarda **tamsayı**
değişken için `n` ve `f(n), g(n)` kullanılır. f(n) karmaşık fonksiyon, g(n) onu sınırlayan daha
basit fonksiyondur.
:::

:::exam Kesin bilinmesi gerekenler: sadeleştirme kuralları (sabit at, en yüksek terim);
büyüme fonksiyonu sıralaması; O/Ω/Θ ↔ worst/best/average; graf algoritmaları Big-O tablosu
(BFS/DFS O(V+E), Floyd-Warshall O(V³), Dijkstra, Bellman-Ford O(VE)).
:::
""",
"qa": [
 ("Big O notasyonu nedir ve neyi tanımlar?",
  "**Big O notasyonu**, bir algoritmanın **verimliliğini**, yani **girdi boyutu (n) büyüdükçe** çalışma süresinin (veya bellek kullanımının) nasıl büyüdüğünü tanımlayan standart bir yöntemdir. Algoritmaların ölçeklenebilirliğini karşılaştırmayı sağlar. Genellikle **worst case** (en kötü durum) büyüme hızını ifade eder ve sabit donanım/dil farklarından bağımsızdır."),
 ("Bir algoritmanın Big O karmaşıklığı hangi adımlarla hesaplanır?",
  "(1) Performansı etkileyen **girdi boyutu n**'i belirle. (2) Zaman karmaşıklığına katkı yapan **temel işlemleri say**. (3) İşlem sayısını **n cinsinden bir fonksiyon** olarak ifade et. (4) **Sadeleştir:** sabit katsayıları at (`O(2n)→O(n)`) ve yalnızca **en yüksek dereceli terimi** tut (`O(n²+n)→O(n²)`)."),
 ("Big O sadeleştirmesinin iki temel kuralı nedir? Örnek verin.",
  "(1) **Sabitleri/katsayıları at:** `O(2n) → O(n)`, `O(½n²) → O(n²)`. (2) **Yalnızca en yüksek dereceli terimi tut:** `O(n² + n) → O(n²)`, `O(n³ + 100n²) → O(n³)`. Sebep: n büyüdükçe en yüksek dereceli terim baskın hale gelir ve sabitler büyüme **oranını** değiştirmez. Yani `O(3n² + 5n + 7)` sadeleşince **O(n²)** olur."),
 ("Big O, Big Ω ve Big Θ sırasıyla hangi durumu (case) tanımlar?",
  "**Big O** → **worst case** (en kötü durum), üst sınır: ifadeden daha yavaş ya da aynı hızda büyüyen fonksiyonlar. **Big Ω** → **best case** (en iyi durum), alt sınır: daha hızlı ya da aynı hızda büyüyenler. **Big Θ** → **average case**: fonksiyon hem O hem Ω içindeyse, yani alttan ve üstten aynı oranla sınırlıysa kullanılan **sıkı (tight) sınır**dır."),
 ("Aşağıdaki graf algoritmalarının Big O zaman karmaşıklıkları nedir: BFS, DFS, Bellman-Ford, Floyd-Warshall?",
  "**BFS: O(V + E)**, **DFS: O(V + E)** (her düğüm ve kenar bir kez işlenir). **Bellman-Ford: O(V·E)** (V−1 tur × E kenar). **Floyd-Warshall: O(V³)** (tüm düğüm çiftleri için üçlü iç içe döngü). Ek olarak: Dijkstra O(V²) veya O(E log V), Prim ve Kruskal O(E log V), Topological Sort O(V + E)."),
 ("Büyüme fonksiyonlarını küçükten büyüğe sıralayın: n², 2ⁿ, log n, n log n, 1, n, n³.",
  "Küçükten büyüğe: **O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)**. Yani sabit en yavaş, üstel (`2ⁿ`) en hızlı büyür. İyi algoritmalar mümkün olduğunca soldaki sınıflarda kalır; `O(n²)` ve üzeri büyük girdiler için pahalıdır, `O(2ⁿ)` yalnızca çok küçük n için pratiktir."),
 ("`O(2n + 3)` ifadesi neye sadeleşir ve neden?",
  "**O(n)**'e sadeleşir. Çünkü Big O'da (1) **sabit toplananlar atılır** (`+3` düşer) ve (2) **sabit katsayılar atılır** (`2n`'deki 2 düşer). Geriye büyüme **oranını** belirleyen terim, yani `n` kalır. Sabitler donanıma/uygulamaya göre değişir ama büyüme hızını (lineer olmasını) değiştirmez; bu yüzden `O(2n+3) = O(n)`'dir."),
]
})

print("NEW L1-L5 loaded:", len(NEW))
