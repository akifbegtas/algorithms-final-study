# -*- coding: utf-8 -*-
# Tüm ders içerikleri: konu anlatımı (kod gömülü) + her ders 7 soru-cevap.

LECTURES = []

# ===========================================================================
# L1 — C++'a Giriş
# ===========================================================================
LECTURES.append({
"code": "L1",
"title": "C++'a Giriş — Temel Yapılar",
"subtitle": "cout/cin, namespace, değişkenler, switch, döngü, dizi, sınıf ve constructor",
"body": r"""
Bu ders dersin geri kalanının dili olan **C++**'ın temellerini kuruyor. Sınavda doğrudan
"bu kodun çıktısı ne?" ya da "şu satır ne işe yarar?" diye sorulur.

## Bir C++ programının iskeleti
`#include <iostream>` giriş/çıkış nesnelerini (`cout`, `cin`) getiren bir **header** dosyasıdır.
`using namespace std;` ise `std::cout` yerine sadece `cout` yazabilmemizi sağlar; standart
kütüphanedeki isimleri çıplak kullanmamıza izin verir.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Merhaba Dunya" << endl;   // ekrana yaz
    return 0;
}
```

`endl` ile `\n` ikisi de satır atlatır; ancak `endl` ek olarak **buffer'ı flush eder**
(tamponu boşaltır), bu yüzden `\n`'den biraz daha yavaştır.

## namespace nedir?
Bir **namespace**, değişken/fonksiyon/sınıf gibi isimleri gruplayıp **isim çakışmalarını**
(name collision) önleyen bir mekanizmadır. Aynı isim farklı namespace'lerde çakışmadan
bulunabilir. `std` standart kütüphanenin namespace'idir.

## Değişkenler ve kullanıcıdan girdi
```cpp
int sayi;
cout << "Bir sayi gir: ";
cin >> sayi;                 // klavyeden oku
cout << "Karesi: " << sayi * sayi << endl;
```

## switch — çoklu dallanma
`switch` ifadesi **bir kez** değerlendirilir, sonra her `case` ile karşılaştırılır. `break`
olmazsa alttaki case'lere de "düşer" (fall-through). `default` hiçbiri tutmazsa çalışır.

```cpp
switch (secim) {
    case 1: cout << "Toplama";  break;
    case 2: cout << "Carpma";   break;
    default: cout << "Gecersiz secim";
}
```

## while döngüsü
Bir koşul sağlandığı sürece bloğu tekrarlar.

```cpp
int i = 0;
while (i < 5) {
    cout << i << " ";
    i++;                      // i artmazsa SONSUZ döngü olur
}
```

## Diziler (arrays)
Bir dizi, aynı tipten birden çok değeri tek değişkende tutar. **Index 0'dan başlar.**

```cpp
int notlar[4] = {90, 75, 60, 100};
cout << notlar[0];            // 90  (ilk eleman)
cout << notlar[3];            // 100 (son eleman)
```

## Sınıf (class) ve nesne (object)
**Class** bir şablondur; **object** o şablondan üretilen somut örnektir. Üyelere `.` ile erişilir.
**Constructor**, sınıfla aynı ada sahip özel bir metottur ve nesne **oluşturulduğu anda
otomatik** çağrılır.

```cpp
class Ogrenci {
public:
    string ad;
    int no;
    Ogrenci(string a, int n) {   // constructor
        ad = a;
        no = n;
    }
    void yaz() {                  // metot
        cout << no << " - " << ad << endl;
    }
};

int main() {
    Ogrenci o1("Akif", 101);      // constructor burada çalışır
    o1.yaz();                     // 101 - Akif
}
```

:::exam Sık çıkan kalıplar: namespace tanımı, `endl` vs `\n`, switch'te `break` unutulması,
dizide index 0, constructor'ın ne zaman çağrıldığı, ve küçük bir kod parçasının çıktısı.
:::
""",
"qa": [
 ("`using namespace std;` satırı tam olarak ne işe yarar?",
  "`std` standart kütüphanenin **namespace**'idir. Bu satır olmadan `std::cout`, `std::cin`, `std::string` gibi tam nitelikli isimler yazmamız gerekir. `using namespace std;` ile bu isimleri **çıplak** (`cout`, `cin`) kullanabiliriz. Asıl amacı namespace'in kendisi değil, **isim çakışmalarını önlemek**tir: aynı isim farklı namespace'lerde farklı anlamlarla, çakışmadan var olabilir."),
 ("`endl` ile `\\n` arasındaki fark nedir?",
  "İkisi de imleci **yeni satıra** geçirir. Fark: `endl` ek olarak çıkış **buffer'ını flush eder** (tamponu hemen boşaltır), `\\n` ise sadece satır karakteri ekler. Bu yüzden çok sayıda satır yazarken `\\n` **daha hızlıdır**; `endl` gereksiz flush yüzünden yavaşlatabilir."),
 ("`switch` ifadesinde `break` ve `default` anahtar kelimelerinin görevi nedir?",
  "`break` eşleşen `case` çalıştıktan sonra switch'ten **çıkar**. Yazılmazsa program alttaki case'lere de **düşer** (fall-through) ve onları da çalıştırır — çoğu zaman istenmeyen bir hatadır. `default` ise **hiçbir case eşleşmezse** çalışan bloktur; `else` gibidir. İkisi de opsiyoneldir."),
 ("Bir C++ dizisinde ilk ve son elemana nasıl erişilir? `int a[4]` için son index kaçtır?",
  "Diziler **0-tabanlıdır**. İlk eleman `a[0]`, son eleman ise `a[n-1]`'dir. `int a[4]` için geçerli index'ler 0,1,2,3'tür; **son index 3**'tür. `a[4]` yazmak dizi sınırını aşar (out-of-bounds) ve tanımsız davranıştır."),
 ("Class ile object arasındaki fark nedir?",
  "**Class** bir **şablon/plan**dır: hangi veri (attribute) ve davranışlara (method) sahip olunacağını tanımlar ama bellekte yer kaplamaz. **Object**, o sınıftan `ClassName nesne;` ile üretilen **somut bir örnektir** ve gerçekten bellekte yer kaplar. Örn. `Ogrenci` sınıftır, `o1` ve `o2` ondan üretilmiş nesnelerdir. Nesne üyelerine `nesne.uye` (nokta) ile erişilir."),
 ("Constructor nedir ve ne zaman çağrılır?",
  "**Constructor**, sınıfla **aynı ada** sahip, dönüş tipi olmayan özel bir metottur. Bir nesne **oluşturulduğu anda otomatik** olarak çağrılır ve genellikle nesnenin başlangıç değerlerini (attribute'ları) atamak için kullanılır. Örn. `Ogrenci o1(\"Akif\", 101);` satırı çalıştığında `Ogrenci(string, int)` constructor'ı tetiklenir."),
 ("Aşağıdaki kodun çıktısı nedir?\n\n```cpp\nint a[3] = {2, 4, 6};\nint t = 0;\nfor (int i = 0; i < 3; i++) t += a[i];\ncout << t << endl;\n```",
  "Döngü dizinin tüm elemanlarını toplar: `2 + 4 + 6 = 12`. Çıktı: **`12`**. (Döngü `i=0,1,2` için çalışır; `i=3`'te `i<3` yanlış olduğu için durur — yani sınır dışına çıkmaz.)"),
]
})

# ===========================================================================
# L2 — Veri Yapıları & Bağlı Listeler
# ===========================================================================
LECTURES.append({
"code": "L2",
"title": "Veri Yapıları ve Bağlı Listeler (Linked List)",
"subtitle": "Lineer/non-lineer yapılar, Stack/Queue, template, node ekleme/silme/arama",
"body": r"""
## Veri yapısı sınıflandırması
Veri yapıları iki büyük gruba ayrılır:
- **Physical (bellek düzeyinde):** Array ve Linked List — verinin bellekte nasıl tutulduğu.
- **Logical (performans/kullanım düzeyinde):** Stack, Queue, Tree, Graph, Hash Table.

Ayrıca **lineer** (Array, Linked List, Stack, Queue) ve **non-lineer** (Tree, Graph) diye de ayrılır.
İki kritik davranış kalıbı:
- **Stack → LIFO** (Last In First Out) — son giren ilk çıkar.
- **Queue → FIFO** (First In First Out) — ilk giren ilk çıkar.

## Bağlı liste (Linked List) nedir?
Bağlı liste, **node** denen elemanların doğrusal kümesidir ve sıralama **pointer**'larla
sağlanır. Her node iki parçadan oluşur:
1. **data** — elemanın değeri,
2. **next** — bir sonraki node'un adresi (link).

**Singly linked list**'te son node'un `next`'i `NULL`'dur (liste sonu).

```cpp
template <class T>      // template: tipi parametre yaparak tek kodu her tip için kullanmak
struct Node {
    T data;
    Node<T>* next;
};
```

:::tip **Template** sayesinde `int`, `double`, `string`... her tip için ayrı ayrı kod yazmayız;
tip bir parametre olur.
:::

## Liste boş mu?
Baş işaretçisi (head) `NULL` ise liste boştur.

```cpp
bool isEmpty(Node<int>* head) {
    return head == NULL;
}
```

## Başa eleman ekleme
```cpp
void addFirst(Node<int>*& head, int deger) {
    Node<int>* yeni = new Node<int>();
    yeni->data = deger;
    yeni->next = head;   // yeni node eski başı gösterir
    head = yeni;         // baş artık yeni node
}
```

## Sona ekleme (insert/append)
İki durum vardır: liste boşsa yeni node hem head hem tail olur; değilse sona eklenir.

```cpp
void append(Node<int>*& head, int deger) {
    Node<int>* yeni = new Node<int>();
    yeni->data = deger;
    yeni->next = NULL;
    if (head == NULL) { head = yeni; return; }
    Node<int>* p = head;
    while (p->next != NULL) p = p->next;  // sona git
    p->next = yeni;
}
```

## Arama (search)
Liste baştan sona gezilir (traverse), her node'un değeri aranan değerle karşılaştırılır.

```cpp
bool search(Node<int>* head, int aranan) {
    Node<int>* p = head;
    while (p != NULL) {
        if (p->data == aranan) return true;
        p = p->next;
    }
    return false;
}
```

## Silme (delete) — dikkat edilecek durumlar
Silmede şu özel durumlar vardır: liste boş; silinecek tek node; **head**'in silinmesi;
**tail**'in silinmesi; ortadaki bir node; ya da eleman listede yok. Head silinirken `head`
bir sonraki node'a kaydırılır:

```cpp
void deleteValue(Node<int>*& head, int hedef) {
    if (head == NULL) return;                 // boş liste
    if (head->data == hedef) {                // baş node siliniyor
        Node<int>* tmp = head;
        head = head->next;
        delete tmp;
        return;
    }
    Node<int>* p = head;
    while (p->next != NULL && p->next->data != hedef) p = p->next;
    if (p->next != NULL) {                     // bulundu
        Node<int>* tmp = p->next;
        p->next = tmp->next;                   // bağı atla
        delete tmp;
    }
}
```

:::exam Sık sorular: Array vs Linked List farkı, node'un iki parçası, Stack=LIFO/Queue=FIFO,
template'in amacı, ekleme/silmede pointer güncelleme sırası.
:::
""",
"qa": [
 ("Bir linked list node'u hangi iki parçadan oluşur?",
  "Her node iki parçadan oluşur: (1) **data** — elemanın değeri/bilgisi, (2) **next** (link/pointer alanı) — listedeki **bir sonraki node'un adresi**. Singly linked list'te son node'un `next` alanı `NULL`'dur ve bu, listenin sonunu temsil eder."),
 ("Array (dizi) ile Linked List arasındaki temel fark nedir?",
  "**Array** bellekte **bitişik (contiguous)** yer kaplar, boyutu genelde sabittir, index ile **O(1)** rastgele erişim sağlar ama araya ekleme/silme elemanları kaydırmayı gerektirir (**O(n)**). **Linked List** node'ları bellekte dağınık durur, pointer'larla bağlanır, **dinamik** büyür; baştan ekleme/silme **O(1)**'dir ama bir elemana erişmek için baştan gezmek gerekir (**O(n)** erişim)."),
 ("Stack ve Queue arasındaki fark nedir? Hangisi LIFO hangisi FIFO?",
  "**Stack → LIFO** (Last In First Out): en son eklenen eleman ilk çıkar (tabak yığını gibi). **Queue → FIFO** (First In First Out): ilk eklenen ilk çıkar (sıra/kuyruk gibi). İkisi de **lineer** mantıksal veri yapılarıdır."),
 ("C++'ta `template` ne işe yarar, bağlı listede neden kullanılır?",
  "**Template**, **veri tipini bir parametre** yaparak aynı kodu farklı tipler için tekrar yazmaktan kurtarır. Bağlı listede `Node<T>` tanımlarsak; `int`, `double`, `string`... her tür için ayrı `Node` sınıfı yazmamıza gerek kalmaz, tek şablon hepsine hizmet eder. Bu **kod tekrarını** azaltır ve tip güvenliğini korur."),
 ("Bir bağlı listede arama (search) nasıl yapılır ve karmaşıklığı nedir?",
  "Liste **baştan sona gezilir** (traverse): `head`'den başlanır, her node'un `data`'sı aranan değerle karşılaştırılır, eşleşme bulunana ya da `NULL`'a (liste sonu) ulaşılana dek `p = p->next` ile ilerlenir. En kötü durumda tüm liste gezilir, dolayısıyla **O(n)**'dir. (Linked list'te ikili arama yapılamaz çünkü rastgele erişim yoktur.)"),
 ("Bir bağlı listenin başındaki (head) node'u silerken hangi adımlar izlenir?",
  "Head silinirken: (1) Geçici bir pointer ile eski head saklanır (`tmp = head`), (2) `head` bir sonraki node'a kaydırılır (`head = head->next`), (3) eski head bellekten serbest bırakılır (`delete tmp`). Sıra önemlidir; önce `delete head` yaparsak `head->next`'e erişimi kaybederiz."),
 ("Listenin başına node eklerken `yeni->next = head;` ve `head = yeni;` satırlarının sırası neden önemlidir?",
  "Önce **yeni node eski başı göstermeli** (`yeni->next = head`), sonra **head yeni node'a taşınmalıdır** (`head = yeni`). Sıra ters olursa (`head = yeni;` önce yapılırsa) eski listenin başına olan tek bağlantı kaybolur ve listenin geri kalanı **bellekte kaybolur** (memory leak / erişilemez hale gelir)."),
]
})

# ===========================================================================
# L3 — Iteration, Induction, Recursion + Selection Sort
# ===========================================================================
LECTURES.append({
"code": "L3",
"title": "Iteration, Induction, Recursion + Selection Sort",
"subtitle": "Toplam notasyonu, tümevarım, özyineleme kuralları, factorial, GCD, seçmeli sıralama",
"body": r"""
## Iteration, Induction, Recursion
Bunlar veri modelleri ve algoritmaların temel kavramlarıdır:
- **Iteration (yineleme):** İşlemleri `for`/`while` gibi döngülerle tekrarlama.
- **Induction (tümevarım):** Bir ifadeyi tüm `n` için ispatlama yöntemi.
- **Recursion (özyineleme):** Fonksiyonun **kendini çağırması**.

## Toplam (Summation) notasyonu
Büyük Sigma (Σ) bir toplamı gösterir. Örn. `1 + 2 + ... + n` için:
`Σ_{i=1}^{n} i = n(n+1)/2`.

## Tümevarım (Induction) üç adımı
1. **Basis (temel):** En küçük durum doğru mu? Örn. `F(0)` ya da `F(1)`.
2. **Hypothesis (hipotez):** `k ≤ n` için doğru olduğunu **varsay**.
3. **Step (adım):** `n+1` için de doğru olduğunu **göster**.

## Özyinelemenin (Recursion) kuralları
- **Mutlaka bir base case (temel durum) olmalı** — özyinelemesiz hesaplanabilen durum.
- Her özyinelemeli çağrı **base case'e doğru ilerlemeli** (küçülmeli).
- Tüm özyinelemeli çağrıların çalıştığını varsay.
- Aynı problemi farklı çağrılarda tekrar çözüp **işi tekrarlama**.

### Factorial (n!) — özyinelemeli
`n! = n × (n-1)!`, temel durum `1! = 1`.

```cpp
int factorial(int n) {
    if (n <= 1) return 1;          // base case
    return n * factorial(n - 1);   // inductive (recursive) case
}
```

### Euclid GCD (En Büyük Ortak Bölen)
`gcd(u, v) = gcd(v, u % v)`, `v == 0` olunca cevap `u`'dur.

```cpp
int gcd(int u, int v) {
    if (v == 0) return u;          // base case
    return gcd(v, u % v);          // küçülen argümanlarla çağrı
}
// cout << gcd(461952, 116298);
```

## Recursion vs Iteration — dezavantajlar
Recursion **stack** üzerinde fazladan yer harcar (her çağrı ve yerel değişkenler yığında tutulur),
çok derinleşirse **bellek tükenebilir**, ve genelde hız/çalışma süresi açısından döngü kadar
verimli değildir. Bu yüzden tüm elemanlar üzerinde basit bir döngü yetiyorsa recursion'dan kaçınılır.

## Sıralama (Sorting) problemi
Sıralama, bir listeyi belirli bir düzene (artan/sözlük) koymaktır. Çıktı iki koşulu sağlamalı:
(1) **azalmayan** (non-decreasing) sırada olmalı, (2) girdinin bir **permütasyonu** olmalı.

## Selection Sort (Seçmeli Sıralama)
Dizi hayali olarak **sıralı** ve **sırasız** iki parçaya ayrılır. Her adımda sırasız kısmın
**en küçüğü** bulunup sıralı kısmın sonuna konur (i. pozisyonla swap).

```cpp
void selectionSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int small = i;                       // şimdilik en küçük i
        for (int j = i + 1; j < n; j++)
            if (A[j] < A[small]) small = j;  // daha küçüğünü bul
        int temp = A[small];                 // swap A[i] <-> A[small]
        A[small] = A[i];
        A[i] = temp;
    }
}
```

Selection sort'un **loop invariant**'i `S(k)`: "Dış döngünün i. adımında, iç döngüye `j = k`
değeriyle girildiğinde `small`, `A[i..k-1]` aralığının en küçüğünün index'idir." Karmaşıklığı
her durumda **O(n²)**'dir (best/worst/average aynı).

:::exam Çıkan sorular: recursion'da base case zorunluluğu, recursion'ın stack maliyeti, GCD'nin
çalışması, selection sort'un adımları ve O(n²) karmaşıklığı, swap için neden `temp` gerektiği.
:::
""",
"qa": [
 ("Özyinelemeli (recursive) bir fonksiyonun sahip olması gereken iki temel kural nedir?",
  "(1) **Mutlaka bir base case (temel durum) olmalı** — özyineleme olmadan doğrudan değer döndüren durum (örn. `factorial`'da `n<=1`). (2) **Her özyinelemeli çağrı base case'e doğru ilerlemeli** — yani problem her adımda küçülmeli. Bu iki kural sağlanmazsa fonksiyon **sonsuz** özyinelemeye girer ve stack taşar (stack overflow)."),
 ("Euclid GCD algoritması hangi matematiksel gerçeğe dayanır? `gcd(48, 18)` adımlarını yazın.",
  "Dayandığı gerçek: `gcd(u, v) = gcd(v, u mod v)` ve `gcd(u, 0) = u`. Adımlar: `gcd(48,18) = gcd(18, 48%18=12) = gcd(12, 18%12=6) = gcd(6, 12%6=0) = 6`. Sonuç **6**. Her adımda argümanlar küçülür ve `v=0` base case'ine ulaşılır."),
 ("Tümevarım (induction) ispatının üç adımı nedir?",
  "(1) **Basis (temel):** En küçük durum için ifadenin doğruluğu gösterilir (örn. `n=0` veya `n=1`). (2) **Hypothesis (hipotez):** İfadenin keyfi bir `k ≤ n` için doğru olduğu **varsayılır**. (3) **Inductive step (adım):** Hipotez kullanılarak ifadenin `n+1` için de doğru olduğu **kanıtlanır**. Bu üçü sağlanınca ifade tüm `n` için doğrudur."),
 ("Recursion'ın iteration'a göre dezavantajları nelerdir?",
  "Recursion: (1) Her çağrı ve yerel değişkenler **stack**'te tutulduğu için **daha fazla bellek** harcar; (2) çağrılar kontrol edilmezse **bellek tükenebilir** (stack overflow); (3) hız/çalışma süresi açısından genelde döngü kadar verimli değildir; (4) önlem alınmazsa **sonlanmayan** çağrılara yol açabilir. Bu yüzden basit bir döngü yetiyorsa iteration tercih edilir."),
 ("Selection Sort nasıl çalışır? Adımlarını özetleyin.",
  "Dizi hayali olarak **sıralı** ve **sırasız** iki bölüme ayrılır; başta sıralı kısım boştur. Her adımda **sırasız kısmın en küçük elemanı** bulunur ve sırasız kısmın **ilk pozisyonundaki** elemanla yer değiştirilir (swap). Böylece sıralı kısım bir eleman büyür. Sırasız kısım bitince algoritma durur. Toplam `n-1` geçiş yapılır."),
 ("Selection Sort'ta iki elemanı takas etmek (swap) için neden geçici bir `temp` değişkeni gerekir?",
  "`A[i]` ve `A[small]`'ı doğrudan birbirine atarsak (`A[i]=A[small]; A[small]=A[i];`) ilk atamada `A[i]`'nin eski değeri **kaybolur** ve ikinci atama yanlış olur. Bu yüzden bir değer geçici olarak saklanır: `temp = A[small]; A[small] = A[i]; A[i] = temp;`. `temp` olmadan iki değeri güvenle takas etmek mümkün değildir (aritmetik hileler hariç)."),
 ("Selection Sort'un zaman karmaşıklığı nedir ve girdinin sıralı olması bunu değiştirir mi?",
  "Selection Sort her durumda **O(n²)**'dir: dış döngü `n-1` kez, iç döngü ortalama `n/2` kez çalışır → yaklaşık `n²/2` karşılaştırma. Girdi zaten sıralı olsa bile **en küçüğü bulmak için iç döngü yine tüm sırasız kısmı tarar**. Yani best/average/worst hepsi **Θ(n²)**'dir. (Avantajı: en fazla `n-1` swap yapması.)"),
]
})

# ===========================================================================
# L4 — Big O, Big Omega, Big Theta
# ===========================================================================
LECTURES.append({
"code": "L4",
"title": "Big O, Big Ω, Big Θ — Karmaşıklık Analizi",
"subtitle": "Büyüme fonksiyonları, T(n), üst/alt/sıkı sınır, ispatlar, iç içe döngüler",
"body": r"""
## Algoritma karmaşıklığı
Karmaşıklık, bir algoritmanın girdi boyutu `n`'e göre harcadığı **zaman** ve/veya **bellek**
miktarının ölçüsüdür. Üç durum ölçülür:
- **Best case:** en az adım,
- **Worst case:** en çok adım,
- **Average case:** ortalama adım.

## Büyüme fonksiyonları (küçükten büyüğe)
`1 < log n < n < n log n < n² < n³ < 2ⁿ`
- **O(1) Sabit:** girdiye bağlı değil.
- **O(log n) Logaritmik:** problemi her adımda sabit oranda küçültür (örn. binary search).
- **O(n) Lineer:** her eleman için sabit iş.
- **O(n log n):** böl-yönet (merge sort).
- **O(n²) Karesel:** çift iç içe döngü (tüm ikililer).
- **O(n³) Kübik:** üçlü iç içe döngü.
- **O(2ⁿ) Üstel:** pratikte sadece çok küçük `n`.

## Üç sınır (bound) — tanımlar
- **Big-O (üst sınır / worst case):** `f(n) = O(g(n))` ⟺ öyle bir `c>0` ve `n₀` vardır ki
  her `n ≥ n₀` için `f(n) ≤ c·g(n)`. (g, f'i **yukarıdan** sınırlar.)
- **Big-Ω (alt sınır / best case):** `f(n) ≥ c·g(n)` (g, f'i **aşağıdan** sınırlar.)
- **Big-Θ (sıkı sınır / average):** Hem O hem Ω; `c₁·g(n) ≤ f(n) ≤ c₂·g(n)`.

:::tip `n₀`, sınırın geçerli olmaya başladığı **minimum** değerdir; daha büyük her değer de işe yarar.
:::

## T(n) — gerçek adım sayısı
`T(n)`, algoritmanın bir girdide attığı **gerçek adım sayısıdır**; `O(...)` ise **karmaşıklık
sınıfıdır**. `T(n) = O(f(n))`, "T(n) en fazla f(n) karmaşıklığındadır" demektir.

```text
1. n = read input            -> 1
2. sum = 0                   -> 1
3. i = 0                     -> 1
4. while i < n               -> n+1
5.   number = read input     -> n
6.   sum = sum + number      -> n
7.   i = i + 1               -> n
8. mean = sum / n            -> 1
```
Toplam: `T(n) = 4n + 5`. Döngü içi her şey `n` kez çalışır. Sonuç: **T(n) = O(n)**.

## İspat örnekleri
**`4n + 5 = O(n)`:** `f(n) ≤ c·n` için bir `c` arıyoruz. `c=4` yetmez (`4n+5 > 4n`).
`c=8` seçersek `4n + 5 ≤ 8n` (n≥1 için) doğru → `O(n)`.

**`n² + 3n − 1 = O(n²)`:** `< n² + 3n ≤ n² + 3n² = 4n²` → `c=4` ile `O(n²)`.

**Polinomun en yüksek dereceli terimi:** `2n⁷ − 6n⁵ + 10n² − 5 = O(n⁷)`. Her polinom, en
yüksek dereceli teriminin Big-O'sudur; sabitler ve düşük dereceli terimler atılır.

## İç içe döngüler (nested loops)
İç döngü O(n), dış döngü O(n) ise toplam **O(n × n) = O(n²)**. Üçlü iç içe → **O(n³)**.

```cpp
for (int i = 0; i < n; i++)        // dış: n kez
    for (int j = 0; j < n; j++)    // iç: her i için n kez
        cout << i * j << " ";      // toplam n*n = O(n^2)
```

:::exam Mutlaka: O/Ω/Θ'nin best/worst/average karşılığı, en yüksek dereceli terim kuralı,
T(n)=4n+5 örneği, c ve n₀ bulma, iç içe döngülerin çarpımı.
:::
""",
"qa": [
 ("Big-O, Big-Ω ve Big-Θ sırasıyla hangi durumu (case) tanımlar?",
  "**Big-O** → **üst sınır / worst case** (en kötü durum): fonksiyon en fazla bu kadar büyür. **Big-Ω** → **alt sınır / best case** (en iyi durum): en az bu kadar büyür. **Big-Θ** → **sıkı sınır / average case**: fonksiyon hem O hem Ω olduğunda, yani aynı büyüme oranına alttan ve üstten sıkıştığında kullanılır (`c₁g(n) ≤ f(n) ≤ c₂g(n)`)."),
 ("`f(n) = O(g(n))` ifadesinin biçimsel (formal) tanımı nedir?",
  "`f(n) = O(g(n))` demek: öyle pozitif sabitler **c** ve **n₀** vardır ki, **her n ≥ n₀** için `f(n) ≤ c · g(n)` olur. Yani belirli bir noktadan (`n₀`) sonra `g(n)`'in bir katı `f(n)`'i hep üstten sınırlar. `n₀`, sınırın geçerli olmaya başladığı minimum değerdir; daha büyük değerler de geçerlidir."),
 ("`f(n) = 4n + 5` için `f(n) = O(n)` olduğunu nasıl ispatlarsınız?",
  "`f(n) ≤ c·n` olacak bir sabit `c` bulmalıyız. `c=4` işe yaramaz çünkü `4n+5` asla `4n`'den küçük olmaz. `c=8` seçersek: `n≥1` için `4n + 5 ≤ 4n + 4n = 8n` doğrudur (5 ≤ 4n, n≥2 için; n=1'de 8·1=8 ≥ 9 değil, bu yüzden n₀ ayarı veya c=9 da denebilir — slayttaki kabul c=8). Tüm n için geçerli bir c bulunduğundan `T(n) = O(n)`'dir."),
 ("Bir polinomun Big-O'su nasıl bulunur? `2n⁷ − 6n⁵ + 10n² − 5` neyin O'sudur?",
  "Kural: **her polinom, en yüksek dereceli teriminin Big-O'sudur.** Sabit çarpanlar ve düşük dereceli terimler atılır. `2n⁷ − 6n⁵ + 10n² − 5 = O(n⁷)`. (İspat: katsayıların mutlak değerini al, tüm terimleri en yüksek dereceye yükselt: `2n⁷+6n⁷+10n⁷ = 18n⁷`, yani `c=18` ile `O(n⁷)`.)"),
 ("T(n) fonksiyonu ile O(f(n)) gösterimi arasındaki fark nedir?",
  "**T(n)**, algoritmanın `n` boyutlu girdide attığı **gerçek adım sayısıdır** (örn. `T(n)=4n+5`). **O(f(n))** ise bir **karmaşıklık sınıfıdır** — büyüme hızını niteler. `T(n)=O(f(n))` yazmak, \"T(n)'in karmaşıklığı en fazla f(n) kadardır\" demektir. Kısaca T(n) somut sayı, O soyut sınıftır; karıştırılmamalıdır."),
 ("İç içe iki döngünün (her biri n kez) toplam karmaşıklığı nedir, neden?",
  "**O(n²)**. Dış döngü `n` kez döner; **dış döngünün her bir turunda** iç döngü baştan `n` kez döner. Toplam iş `n × n = n²`'dir. Genel kural: iç içe döngülerde karmaşıklıklar **çarpılır** (ardışık/peş peşe döngülerde ise **toplanır**, ama Big-O'da en büyüğü baskındır). Üç iç içe → O(n³)."),
 ("Büyüme fonksiyonlarını küçükten büyüğe sıralayın: `n²`, `log n`, `2ⁿ`, `n log n`, `1`, `n`, `n³`.",
  "Küçükten büyüğe: **1 < log n < n < n log n < n² < n³ < 2ⁿ**. Yani sabit en yavaş büyür, üstel (`2ⁿ`) en hızlı büyür. Algoritma seçerken hedef mümkün olduğunca soldaki sınıflarda kalmaktır; `O(n log n)` iyi, `O(n²)` ve üstü büyük girdiler için kötü kabul edilir."),
]
})

# ===========================================================================
# L5 — Bubble, Insertion, Selection Sort
# ===========================================================================
LECTURES.append({
"code": "L5",
"title": "Bubble, Insertion ve Selection Sort",
"subtitle": "Üç adet O(n²) sıralama algoritması — mekanizma, kod, kararlılık (stability)",
"body": r"""
Bu ders **O(n²)** sınıfındaki üç temel sıralama algoritmasını karşılaştırır:
**Bubble, Insertion, Selection**.

## Bubble Sort (Kabarcık Sıralama)
Liste tekrar tekrar gezilir; **komşu ikililer** karşılaştırılır ve ters sıradalarsa **takas** edilir.
Hiç takas olmayan bir geçiş, listenin sıralı olduğunu gösterir. Küçük elemanlar başa doğru
"kabarcık" gibi yükseldiği için bu adı alır.

```cpp
void bubbleSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (A[j] > A[j + 1]) {          // komşuları karşılaştır
                int t = A[j]; A[j] = A[j + 1]; A[j + 1] = t;  // swap
                swapped = true;
            }
        }
        if (!swapped) break;                // takas yoksa sıralıdır -> dur
    }
}
```

## Insertion Sort (Eklemeli Sıralama)
Sıralı bir alt liste **birer birer** büyütülür; her yeni eleman, sıralı kısımda **doğru yerine
kaydırılarak** yerleştirilir. Avantajları: basit; küçük veri setlerinde verimli; **adaptive**
(neredeyse sıralı veride hızlı, `O(n+d)` — d ters çift sayısı); **stable**; **in-place** (O(1) ek
bellek); **online** (veriyi alırken sıralayabilir). Dizi zaten sıralıysa eleman başına tek
karşılaştırma yeter → **O(n)**.

```cpp
void insertionSort(int A[], int n) {
    for (int i = 1; i < n; i++) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > key) {  // key'den büyükleri sağa kaydır
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = key;                 // key'i yerine koy
    }
}
```

## Selection Sort (Seçmeli Sıralama)
Her adımda kalan (sırasız) kısmın **en küçüğü** bulunup öne alınır. In-place'tir, her durumda
**O(n²)**'dir ve genelde insertion sort'tan biraz daha kötü performans verir.

```cpp
void selectionSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++)
            if (A[j] < A[min]) min = j;
        int t = A[min]; A[min] = A[i]; A[i] = t;   // swap
    }
}
```

## Karşılaştırma özeti
- Üçü de **comparison sort**'tur ve worst-case **O(n²)**'dir.
- **Insertion** en iyi durumda **O(n)** (sıralı veri), **adaptive** ve **stable**.
- **Bubble** en iyi durumda (optimize edilmişse) O(n), ama pratikte en yavaşı.
- **Selection** her durumda O(n²) ama **en az swap** (n-1) yapar; stable değildir.

:::exam Karıştırılan noktalar: hangisi adaptive/stable/online, en iyi durum karmaşıklıkları,
"komşuları karşılaştırıp takas" (bubble) vs "en küçüğü seç" (selection) vs "doğru yere ekle"
(insertion) ayrımı.
:::
""",
"qa": [
 ("Bubble Sort nasıl çalışır ve adını nereden alır?",
  "Bubble Sort listeyi tekrar tekrar gezer, **komşu (adjacent) eleman çiftlerini** karşılaştırır ve ters sıradalarsa **takas eder** (swap). Hiç takasın olmadığı bir geçiş, listenin **sıralı** olduğunu gösterir ve algoritma durur. Adını, küçük elemanların her geçişte listenin başına doğru **kabarcık gibi yükselmesinden** alır. Worst-case karmaşıklığı **O(n²)**'dir."),
 ("Insertion Sort'un sağladığı başlıca avantajlar nelerdir?",
  "Insertion Sort: **basit** implementasyona sahiptir; **küçük** veri setlerinde verimlidir; **adaptive**'tir (neredeyse sıralı veride çok hızlı, `O(n+d)` — d ters çift/inversion sayısı); **stable**'dır (eşit anahtarların sırasını bozmaz); **in-place**'tir (sadece O(1) ek bellek); ve **online**'dır (elemanları alırken sıralayabilir). Sıralı bir dizide eleman başına tek karşılaştırma yapar → **O(n)**."),
 ("Insertion Sort'un en iyi (best case) ve en kötü (worst case) zaman karmaşıklığı nedir?",
  "**Best case O(n):** dizi zaten (neredeyse) sıralıysa, her eleman için iç `while` koşulu hemen yanlış olur, eleman başına tek karşılaştırma yapılır. **Worst case O(n²):** dizi ters sıralıysa her eleman tüm sıralı kısmın başına kadar kaydırılır. Bu **adaptive** davranış, insertion sort'u bubble/selection'dan pratikte üstün kılar."),
 ("Selection Sort ile Bubble Sort arasındaki temel mekanizma farkı nedir?",
  "**Bubble Sort** komşu çiftleri **karşılaştırıp takas ederek** çalışır; her geçişte en büyük eleman sona \"taşınır\" ve çok sayıda takas yapılır. **Selection Sort** ise her geçişte sırasız kısmın **en küçüğünü tek seferde bulur** ve doğru pozisyondaki elemanla **bir kez** takas eder. Sonuç: Selection en fazla `n-1` swap yapar, Bubble çok daha fazla."),
 ("Bir sıralama algoritmasının \"stable\" (kararlı) olması ne demektir? Bu üç algoritmadan hangileri stable'dır?",
  "**Stable** sıralama, **eşit anahtara** sahip elemanların **göreli sırasını korur** (önce gelen önce kalır). Bu, kayıtların ikincil bir alana göre önceden sıralı tutulması gerektiğinde önemlidir. **Insertion Sort** ve (klasik) **Bubble Sort stable**'dır; **Selection Sort** ise standart hâliyle **stable değildir** (uzak takaslar göreli sırayı bozabilir)."),
 ("Üç algoritmanın da ortak zaman karmaşıklığı sınıfı nedir ve neden \"in-place\" sayılırlar?",
  "Üçü de **comparison-based** sıralamadır ve **worst-case O(n²)** sınıfındadır; bu yüzden büyük listelerde merge/quick/heap sort'a göre verimsizdirler. **In-place**'tirler çünkü sıralamayı dizinin kendi içinde, yalnızca **sabit miktarda O(1) ek bellek** (birkaç geçici değişken) kullanarak yaparlar; ekstra bir dizi açmazlar."),
 ("Aşağıdaki insertion sort iç döngüsünde `A[j] > key` koşulu `A[j] < key` yapılırsa ne olur?",
  "Koşul ters çevrilirse sıralama yönü de tersine döner: eleman, kendisinden **küçük** olanların önüne kaydırılır ve sonuçta dizi **azalan (descending)** sırada sıralanır. Yani `>` artan (ascending), `<` azalan sıralama üretir. Mantık aynı kalır, sadece karşılaştırma yönü değişir."),
]
})

# ===========================================================================
# L6 — Algorithm Analysis T(n) & Summation
# ===========================================================================
LECTURES.append({
"code": "L6",
"title": "Algoritma Analizi — T(n) ve Toplam Denklemleri",
"subtitle": "İşlem sayma, maliyet modeli, döngülerden T(n), log kuralları",
"body": r"""
## Algoritmaları matematikle analiz etmek
Algoritmaları **belirli bir bilgisayardan/uygulamadan bağımsız** analiz ederiz. Yöntem:
1. Çözümdeki **anlamlı işlem (significant operation)** sayısını say.
2. Verimi **büyüme fonksiyonlarıyla** ifade et.

## Maliyet (cost) modeli
Her işlemin bir maliyeti vardır ve sabit zaman alır:
```text
count = count + 1;   // Maliyet: c1
sum   = sum + count; // Maliyet: c2
Toplam = c1 + c2     // sabit -> O(1)
```

## Döngülerden T(n) çıkarma (summation)
Bir döngü gövdesi `n` kez çalışıyorsa toplam maliyet `Σ` ile bulunur. Tipik kalıplar:

```cpp
// (1) Tek döngü: gövde n kez
for (int i = 0; i < n; i++)
    x++;                 // T(n) = n*c  ->  O(n)
```
`Σ_{i=0}^{n-1} c = c·n` → **T(n) = cn**, yani **O(n)**.

```cpp
// (2) i=1..n-1 arası: gövde n-1 kez
for (int i = 1; i < n; i++)
    x++;                 // T(n) = c(n-1) -> O(n)
```

```cpp
// (3) İç içe: dış n, iç n -> n^2
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        x++;             // T(n) = c*n^2 -> O(n^2)
```

```cpp
// (4) Üçgen döngü: iç döngü i'ye bağlı
for (int i = 0; i < n; i++)
    for (int j = 0; j < i; j++)
        x++;             // Σ i = n(n-1)/2 -> O(n^2)
```

## Logaritma ve log-zaman
Çoğu böl-yönet algoritmasının büyüme hızı **logaritmiktir**. Temel ilişki:
`n = 2^k ⟺ log₂ n = k`. Yani `log₂ n`, `n`'i 1'e indirene kadar **kaç kez 2'ye böldüğümüzdür**.

```cpp
// Her adımda n yarıya iniyor -> O(log n)
for (int i = n; i > 1; i = i / 2)
    x++;                 // T(n) ≈ log2(n)
```

## Çalışma süresini ölçeklendirme
Slayttaki kural: `New Time = Old Time × f(New n) / f(Old n)`. Örn. `f(n)=n`, eski n=8, yeni n=16,
eski süre 1 sn → yeni süre `1 × 16/8 = 2 sn`. (Lineer algoritma; girdi 2 katına çıkınca süre 2 katı.)

## Matematik kuralları (sık kullanılan)
- `Σ_{i=1}^{n} 1 = n`
- `Σ_{i=1}^{n} i = n(n+1)/2`
- `Σ_{i=1}^{n} i² = n(n+1)(2n+1)/6`
- `log(ab) = log a + log b`, `log(aⁿ) = n log a`, `a^{log_a n} = n`

:::exam Bu ders pür "T(n) hesapla" dersidir. Döngü sınırlarına dikkat: `i<n` → n kez, `i<=n` → n+1 kez,
`j<i` → üçgensel toplam. Yarıya bölen döngü → log n.
:::
""",
"qa": [
 ("`for (int i = 0; i < n; i++) x++;` döngüsünün T(n) ve Big-O karşılığı nedir?",
  "Gövde (`x++`) `i = 0,1,...,n-1` için, yani tam **n kez** çalışır. `T(n) = Σ_{i=0}^{n-1} c = c·n`. Dolayısıyla **T(n) = cn** ve **O(n)** (lineer). Sabit `c` Big-O'da atılır."),
 ("`for (i=0;i<n;i++) for (j=0;j<i;j++) x++;` üçgen döngüsünün karmaşıklığı nedir?",
  "İç döngü, dış döngünün her `i` değeri için `i` kez çalışır. Toplam iş `Σ_{i=0}^{n-1} i = 0+1+2+...+(n-1) = n(n-1)/2`. Bu `(n²−n)/2`'dir; baskın terim `n²` olduğundan **O(n²)**'dir. (Tam `n²` değil ama Big-O olarak aynı sınıf.)"),
 ("`log₂ n = k` ifadesi sezgisel olarak ne anlatır?",
  "`n = 2^k ⟺ log₂ n = k` ilişkisi şunu söyler: **log₂ n, n'i 1'e indirene kadar kaç kez 2'ye böldüğümüzdür** (ya da 1'den n'e ulaşmak için kaç kez 2 ile çarptığımızdır). Örn. `log₂ 16 = 4` çünkü 16→8→4→2→1, 4 bölme. Bu yüzden girdiyi her adımda yarıya indiren algoritmalar **O(log n)**'dir."),
 ("Bir algoritma O(n) ve n=8 için 1 saniye sürüyorsa, n=16 için tahmini süre nedir?",
  "Kural: `Yeni Süre = Eski Süre × f(Yeni n) / f(Eski n)`. `f(n)=n` (lineer) olduğundan: `1 × 16/8 = 2 saniye`. Lineer bir algoritmada girdi iki katına çıkınca süre de yaklaşık **iki katına** çıkar. (Eğer O(n²) olsaydı `1 × 16²/8² = 4 sn` olurdu.)"),
 ("`for (i = n; i > 1; i = i/2) x++;` döngüsü kaç kez döner, karmaşıklığı nedir?",
  "`i` her adımda **yarıya** iner: n → n/2 → n/4 → ... → 1. Bu, `i` 1'e ulaşana kadar `log₂ n` adım sürer. Dolayısıyla döngü yaklaşık **log₂ n** kez döner ve karmaşıklık **O(log n)**'dir. Yarıya bölme/iki katına çıkma, logaritmik davranışın klasik işaretidir."),
 ("`Σ_{i=1}^{n} i` ve `Σ_{i=1}^{n} i²` toplamlarının kapalı formülleri nelerdir?",
  "`Σ_{i=1}^{n} i = n(n+1)/2` (Big-O: O(n²)) ve `Σ_{i=1}^{n} i² = n(n+1)(2n+1)/6` (Big-O: O(n³)). Bu formüller döngülerin T(n)'ini kapalı forma çevirmek için sık kullanılır; örneğin iç içe döngülerde iç sınır dış değişkene bağlıysa bu toplamlar ortaya çıkar."),
 ("`for (int i = 0; i <= n; i++)` döngüsü gövdesi kaç kez çalışır? `i < n`'den farkı nedir?",
  "`i <= n` için döngü `i = 0,1,...,n` değerlerini alır → **n+1 kez** çalışır. `i < n` ise `i = 0,...,n-1` → **n kez** çalışır. Big-O her ikisinde de O(n)'dir ama **kesin adım sayısı (T(n))** bir fark eder: `<=` bir fazla iterasyon yapar. T(n) hesaplarken sınır koşulu (`<` mi `<=` mi) çok önemlidir."),
]
})

# ===========================================================================
# L7 — Pandas, DataFrame, Matplotlib
# ===========================================================================
LECTURES.append({
"code": "L7",
"title": "Pandas, DataFrame ve Matplotlib",
"subtitle": "Python ile veri analizi: DataFrame oluşturma, temizleme, görselleştirme",
"body": r"""
Bu ders algoritma analizini **görselleştirmek** için Python araçlarını tanıtır: **Pandas
DataFrame** (tablo verisi) ve **Matplotlib** (grafik).

## Standart import'lar
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
**NumPy** matematiksel fonksiyonlar/diziler sağlar; **Pandas** hızlı ve esnek veri analizi
sunar; **Matplotlib** grafik çizer.

## DataFrame nedir?
**İki boyutlu**, boyutu değişebilen, heterojen (farklı tipte sütunlar tutabilen) **tablo**
veri yapısıdır — bir Excel sayfası ya da SQL tablosu gibi. **Sütunlar isimli**, **satırlar
numaralıdır**.

```python
# 5x2 NumPy dizisinden DataFrame
my_data = np.array([[0,3],[10,7],[20,9],[30,14],[40,15]])
cols = ['temperature', 'activity']
df = pd.DataFrame(data=my_data, columns=cols)
print(df)
```

### Yeni sütun ekleme
```python
df["adjusted"] = df["activity"] + 2   # mevcut sütundan türeterek yeni sütun
```

### Veriyi görüntüleme / inceleme
```python
df.head(3)     # ilk 3 satır
df.tail(3)     # son 3 satır
df.info()      # sütun tipleri, null sayıları, bellek
df.iloc[[2]]   # 2 numaralı satır
df[1:4]        # 1,2,3 numaralı satırlar (slice)
df['temperature']  # tek sütun
```

## Veri temizleme (cleaning)
Tipik problemler: **boş hücreler**, **yanlış format**, **yanlış veri**, **duplikeler**.

```python
df.dropna(inplace=True)          # null içeren satırları sil
df.fillna(130, inplace=True)     # null'ları 130 ile doldur
df["Calories"].fillna(df["Calories"].mean(), inplace=True)  # ortalama ile doldur
```
- **Mean** = ortalama, **Median** = sıralı orta değer, **Mode** = en sık görülen değer.

### Duplikeleri bulma/silme
```python
df.duplicated()                  # her satır için True/False
df.drop_duplicates(inplace=True) # tekrar eden satırları sil
```

## Matplotlib ile grafik
`plot()` noktalar arasına çizgi çeker; iki dizi alır (x ve y).

```python
import matplotlib.pyplot as plt
xpoints = [1, 8]
ypoints = [3, 10]
plt.plot(xpoints, ypoints)              # (1,3)'ten (8,10)'a çizgi
plt.plot(xpoints, ypoints, 'o')         # sadece nokta (marker)
plt.scatter([5,7,8], [99,86,87])        # dağılım grafiği
plt.bar(["A","B","C"], [3,8,1])         # çubuk grafik
plt.pie([35,25,25,15])                  # pasta grafik
plt.show()
```
`marker`, `ms` (markersize), `ls`/`linestyle`, `lw` (linewidth), `color`/`c` gibi argümanlarla
biçimlendirilir. `subplot(satır, sütun, index)` ile tek figürde çok grafik gösterilir.

:::exam Sınavda kavramsal sorulur: DataFrame = isimli sütun + numaralı satır; `head/tail/info`
ne yapar; `dropna` vs `fillna`; mean/median/mode tanımı; `plot` vs `scatter` vs `bar`.
:::
""",
"qa": [
 ("Pandas DataFrame nedir? Satır ve sütunları nasıl adlandırılır?",
  "DataFrame, Pandas kütüphanesinin **iki boyutlu, boyutu değişebilen, heterojen** tablo veri yapısıdır — Excel sayfası veya SQL tablosu gibi. Veriyi **hücrelerde** tutar; **sütunlar isimlidir** (örn. 'temperature'), **satırlar numaralıdır** (0,1,2...). Her sütun bir değişkeni/özelliği, her satır bir gözlemi temsil eder ve farklı tipte veri (int, float, string) barındırabilir."),
 ("`head()`, `tail()` ve `info()` metotları ne yapar?",
  "`head(n)` DataFrame'in **baştan** ilk n satırını (başlıklarla) döndürür — hızlı genel bakış için. `tail(n)` **sondan** son n satırı döndürür. `info()` ise veri seti hakkında **meta bilgi** verir: sütun isimleri, her sütunun **tipi**, **null olmayan** değer sayısı ve bellek kullanımı. Veriyi tanımak ve eksik değer var mı görmek için kullanılır."),
 ("Eksik (boş) hücrelerle başa çıkmanın iki temel yolu nedir? İlgili Pandas metotları hangileridir?",
  "(1) **Satırı silmek:** `dropna()` — null içeren satırları kaldırır (büyük veri setlerinde birkaç satır kaybı sorun değildir). (2) **Değer atamak:** `fillna(deger)` — boş hücreleri bir değerle doldurur. Orijinali değiştirmek için `inplace=True` verilir; aksi halde yeni bir DataFrame döner. Sık bir teknik boşlukları sütunun **mean/median/mode** değeriyle doldurmaktır."),
 ("Mean, median ve mode arasındaki fark nedir?",
  "**Mean (ortalama):** tüm değerlerin toplamı / değer sayısı. **Median (ortanca):** değerler küçükten büyüğe sıralandığında **ortadaki** değer (aykırı değerlere dayanıklıdır). **Mode (mod):** en **sık** görülen değer. Eksik veriyi doldururken dağılıma göre uygun olan seçilir (örn. aykırı değer varsa median tercih edilir)."),
 ("Pandas'ta tekrarlanan (duplicate) satırlar nasıl tespit edilip silinir?",
  "**Tespit:** `df.duplicated()` her satır için bir Boolean (True = bu satır daha önce görüldü) döndürür. **Silme:** `df.drop_duplicates()` tekrar eden satırları kaldırır. `inplace=True` verilirse yeni DataFrame döndürmez, doğrudan orijinalden siler. Duplike satırlar aynı kaydın birden çok kez girilmesidir."),
 ("Matplotlib'te `plot()` ile `scatter()` arasındaki fark nedir?",
  "`plot(x, y)` varsayılan olarak noktaları **çizgiyle birleştirir** (line plot); `'o'` gibi format verilirse sadece marker çizer. `scatter(x, y)` ise her gözlem için **bağımsız bir nokta** çizer, noktaları çizgiyle bağlamaz — iki değişken arasındaki **ilişkiyi/dağılımı** görmek için kullanılır. İkisi de aynı uzunlukta x ve y dizileri ister."),
 ("Bir çizgiyi (1,3)'ten (8,10)'a çizmek için `plt.plot`'a hangi iki dizi verilir?",
  "x-koordinatları bir dizi, y-koordinatları ayrı bir dizi olarak verilir: `plt.plot([1, 8], [3, 10])`. Yani **Parametre 1 = x noktaları**, **Parametre 2 = y noktaları**. Matplotlib bunları (1,3) ve (8,10) olarak eşleştirip aralarına çizgi çeker. x verilmezse 0,1,2,... varsayılan index'leri kullanılır."),
]
})

# ===========================================================================
# L8 — Dijkstra's Algorithm
# ===========================================================================
LECTURES.append({
"code": "L8",
"title": "Dijkstra Algoritması — En Kısa Yol",
"subtitle": "Single-source shortest path, greedy, negatif olmayan ağırlıklar",
"body": r"""
## Single-Source Shortest Path (SSSP) problemi
Bir **kaynak** düğümden (source) grafikteki **tüm diğer** düğümlere giden en kısa yolları bulma
problemidir.

## Dijkstra nedir?
- SSSP probleminin **greedy** (açgözlü) bir çözümüdür.
- Yönlü ve yönsüz grafiklerde çalışır; **ancak tüm kenar ağırlıkları negatif olmamalıdır**
  (nonnegative). Negatif ağırlıkta **yanlış** sonuç verir.
- 1956'da Edsger W. Dijkstra tarafından bulundu.

## Sözde kod (pseudocode)
```text
dist[s] <- 0                    // kaynağın mesafesi 0
for all v in V - {s}
    dist[v] <- ∞                // diğerleri sonsuz
S <- ∅                          // ziyaret edilenler (boş)
Q <- V                          // tüm düğümler kuyrukta
while Q ≠ ∅
    u <- ExtractMin(Q, dist)    // en küçük mesafeli düğümü seç
    S <- S ∪ {u}                // u'yu ziyaret edildi işaretle
    for each v in neighbors[u]
        if dist[v] > dist[u] + w(u, v)     // gevşetme (relaxation)
            dist[v] <- dist[u] + w(u, v)
return dist
```

## Çalışma mantığı (relaxation)
Her adımda **ziyaret edilmemiş, en küçük bilinen mesafeye** sahip düğüm `u` seçilir. `u`'nun her
komşusu `v` için **gevşetme** yapılır:
```text
if (d[u] + c(u, v) < d[v])
    d[v] = d[u] + c(u, v)        // daha kısa yol bulundu, güncelle
```
Seçilen düğüm "visited" olur ve bir daha güncellenmez (greedy seçim).

## Karmaşıklık
- Basit (dizi/linked list) implementasyon: **O(|V|² + |E|)**.
- Seyrek (sparse) grafiklerde **binary heap / priority queue** ile: **O((|E| + |V|) log |V|)**.

## Dijkstra vs Bellman-Ford
- Dijkstra **negatif ağırlıkla çalışmaz**; Bellman-Ford çalışır.
- Dijkstra **daha hızlıdır** (`O((E+V)log V)`), Bellman-Ford `O(VE)`.
- Dijkstra **merkezî**; Bellman-Ford dağıtık (distributed) ortamlara uygundur.

## Uygulamalar
Trafik bilgi sistemleri, harita/yol bulma (Google Maps), yönlendirme (routing), hatta
epidemiyolojide bir bireyin başkalarına ulaşma mesafesi.

:::exam Klasik soru: bir grafikte kaynaktan en kısa mesafeleri tablo ile adım adım hesaplama;
"neden negatif ağırlıkta çalışmaz", greedy seçim, relaxation koşulu, karmaşıklık.
:::
""",
"qa": [
 ("Dijkstra algoritması hangi problemi çözer ve hangi yaklaşımı (paradigma) kullanır?",
  "**Single-Source Shortest Path (SSSP)** problemini çözer: tek bir **kaynak** düğümden grafikteki **tüm diğer** düğümlere giden en kısa (minimum maliyetli) yolları bulur. Kullandığı yaklaşım **greedy** (açgözlü)'dür: her adımda o an için en kısa mesafeli ziyaret edilmemiş düğümü seçer ve bu seçimi kesinleştirir."),
 ("Dijkstra algoritması neden negatif ağırlıklı kenarlarda doğru çalışmaz?",
  "Dijkstra **greedy**'dir: bir düğümü en küçük mesafeyle ziyaret ettiğinde o mesafeyi **kesinleşmiş** kabul eder ve bir daha güncellemez. Negatif kenar varsa, **daha sonra** bulunan bir yol o düğüme daha kısa ulaşabilir — ama düğüm zaten 'visited' olduğu için bu düzeltme yapılamaz. Sonuç yanlış olur. Negatif ağırlıklar için **Bellman-Ford** kullanılır."),
 ("Dijkstra'daki 'relaxation' (gevşetme) adımı tam olarak nedir?",
  "Bir `u` düğümünün komşusu `v` için: eğer `u` üzerinden `v`'ye giden yol, `v`'nin mevcut bilinen mesafesinden kısaysa, mesafe güncellenir. Koşul: **`if (d[u] + c(u,v) < d[v]) then d[v] = d[u] + c(u,v)`**. Yani \"u üzerinden daha kısa bir yol bulundu mu?\" kontrolüdür; bulunduysa `v`'nin en kısa mesafesi yenilenir (ve istenirse önceki düğümü kaydedilir)."),
 ("Dijkstra her iterasyonda hangi düğümü seçer?",
  "Her iterasyonda, **henüz ziyaret edilmemiş** (Q kuyruğundaki) düğümler arasından **en küçük bilinen mesafeye** sahip olanı (`ExtractMin`) seçer. Bu düğüm 'current/visited' olarak işaretlenir, komşuları gevşetilir ve bir daha değerlendirilmez. Bu \"her zaman en yakın olanı kesinleştir\" mantığı, algoritmanın greedy doğasıdır."),
 ("Dijkstra algoritmasının zaman karmaşıklığı nedir?",
  "İmplementasyona bağlıdır: düğümleri **basit bir dizi/linked list**'te tutarsak **O(|V|² + |E|)** olur. **Seyrek (sparse)** grafiklerde, grafiği komşuluk listesiyle saklayıp **binary heap / priority queue** kullanırsak **O((|E| + |V|) log |V|)**'ye iner. Yoğun grafiklerde dizi versiyonu, seyrek grafiklerde heap versiyonu daha avantajlıdır."),
 ("Dijkstra ile Bellman-Ford arasındaki üç temel fark nedir?",
  "(1) **Negatif ağırlık:** Bellman-Ford negatif kenarlarla çalışır ve negatif çevrim tespit eder; Dijkstra çalışmaz. (2) **Hız:** Dijkstra `O((E+V)log V)` ile daha hızlı; Bellman-Ford `O(VE)` ile daha yavaş. (3) **Dağıtıklık:** Bellman-Ford dağıtık (distributed, örn. ağ yönlendirme protokolleri) uygulanabilir; Dijkstra merkezî hesaplama gerektirir."),
 ("Dijkstra hangi gerçek dünya uygulamalarında kullanılır?",
  "En yaygın kullanımı **trafik bilgi sistemleri** ve **harita/navigasyon** uygulamalarıdır (Google Maps, MapQuest), **ağ yönlendirme (routing)** sistemleri. Ayrıca epidemiyolojide bir bireyin diğerlerine ne kadar 'yakın' (kaç adım) olduğunu — dolayısıyla hastalık yayma potansiyelini — modellemekte de kullanılır. Genel olarak \"bir kaynaktan optimal yol\" gereken her yerde uygundur."),
]
})

# ===========================================================================
# L9 — Bellman-Ford Algorithm
# ===========================================================================
LECTURES.append({
"code": "L9",
"title": "Bellman-Ford Algoritması",
"subtitle": "Negatif ağırlıklı en kısa yol, relaxation V-1 kez, negatif çevrim tespiti",
"body": r"""
## Bellman-Ford nedir?
Ağırlıklı bir grafikte iki düğüm arası **en kısa yolu** bulan bir **single-source shortest path**
algoritmasıdır (1958, Bellman & Ford). Dijkstra'dan farkı: **negatif ağırlıklı kenarlarla
çalışır** ve **negatif çevrimleri (negative cycle) tespit eder**.

## Çalışma mantığı
Tüm kenarlar üzerinde **V−1 kez** gevşetme (relaxation) yapılır. Her geçişte, daha kısa bir yol
bulunursa düğümün mesafesi ve öncülü (predecessor) güncellenir.

```text
Bellman-Ford(G, w, s)
1. Initialize-Single-Source(G, s)        // dist[s]=0, diğerleri ∞
2. for i = 1 to |V| - 1 do               // V-1 tur
3.     for each edge (u, v) in E do
4.         Relax(u, v, w)
5. for each edge (u, v) in E do           // negatif çevrim kontrolü
6.     if d[v] > d[u] + w(u, v)
7.         return FALSE   // negatif çevrim var
8. return TRUE

Relax(u, v, w):
    if d[v] > d[u] + w(u, v)
        d[v] = d[u] + w(u, v)
        parent[v] = u
```

## Neden V−1 tur?
En kısa yol en fazla **V−1 kenar** içerebilir (döngüsüz). Her tur en az bir düğümün nihai
mesafesini kesinleştirir; bu yüzden **V−1 tur** tüm en kısa yolları bulmaya yeter. V−1 turdan
sonra hâlâ gevşetme yapılabiliyorsa, grafikte **negatif çevrim** vardır.

## Karmaşıklık
- **Zaman: O(V·E)** — V−1 tur × her turda E kenar.
- **Uzay: O(V)** — sadece her düğümün mesafesini saklar.
- Best case (negatif kenar yoksa, erken durdurma ile): yaklaşık O(E).

## Dijkstra ile karşılaştırma
| Özellik | Bellman-Ford | Dijkstra |
|---|---|---|
| Negatif kenar | ✅ Evet | ❌ Hayır |
| Negatif çevrim tespiti | ✅ Evet | ❌ Hayır |
| Hız | O(VE) (yavaş) | O((E+V)log V) (hızlı) |
| Dağıtık | ✅ Kolay | ❌ Merkezî |

## Uygulamalar
Ağ yönlendirme protokolleri (distance-vector routing), trafik akış analizi, havayolu çizelgeleme.

:::exam Slaytta bizzat sorulan sorular: zaman karmaşıklığı **O(VE)**; uzay **O(V)**; Bellman-Ford
negatif kenarı işler, Dijkstra işlemez; en kötü durum analizi; V-1 turun sebebi.
:::
""",
"qa": [
 ("Bellman-Ford'un Dijkstra'ya göre en önemli iki üstünlüğü nedir?",
  "(1) **Negatif ağırlıklı kenarlarla** doğru çalışır (Dijkstra çalışmaz). (2) Grafikte **negatif ağırlıklı çevrim (negative cycle)** olup olmadığını **tespit edebilir** — V−1 turdan sonra hâlâ gevşetme mümkünse negatif çevrim vardır ve en kısa yol tanımsızdır. Bedeli, Dijkstra'dan daha yüksek zaman karmaşıklığıdır (O(VE) vs O((E+V)log V))."),
 ("Bellman-Ford'un zaman ve uzay karmaşıklığı nedir? (Slayttaki cevaplar)",
  "**Zaman karmaşıklığı: O(V·E)** — algoritma V−1 tur döner, her turda tüm E kenarı gevşetir → O(VE). **Uzay karmaşıklığı: O(V)** — yalnızca her düğüm için mesafe (ve öncül) değerini saklar. (Slaytın belirttiği 'worst case O(V³)' yorumu, E ≈ V² olan yoğun grafik için O(VE)=O(V·V²)=O(V³) özel durumudur.)"),
 ("Bellman-Ford neden kenarları tam olarak V−1 kez gevşetir?",
  "Çevrimsiz (simple) bir en kısa yol en fazla **V−1 kenar** içerebilir (V düğüm → en çok V−1 ayrıt). Her gevşetme turu, en kısa yolun bir kenarını daha 'kesinleştirir'; dolayısıyla **V−1 tur** tüm en kısa yolların kesinleşmesi için yeterlidir. V−1 turdan sonra hâlâ bir kenar gevşetilebiliyorsa, bu bir **negatif çevrim** işaretidir."),
 ("Negatif çevrim (negative cycle) nasıl tespit edilir ve neden problem oluşturur?",
  "V−1 turdan **sonra** tüm kenarlar bir kez daha kontrol edilir: eğer hâlâ `d[v] > d[u] + w(u,v)` (yani hâlâ gevşetme mümkün) ise grafikte **negatif çevrim** vardır ve algoritma hata/FALSE döndürür. Problem şudur: negatif toplam ağırlıklı bir çevrimde dönüp durarak mesafe **sonsuza dek azaltılabilir**, bu yüzden 'en kısa yol' tanımsız hale gelir."),
 ("Bellman-Ford'taki Relax(u, v, w) işlemi ne yapar?",
  "Relax, `u` üzerinden `v`'ye giden yolun mevcut en kısa mesafeyi iyileştirip iyileştirmediğini kontrol eder: **`if d[v] > d[u] + w(u,v) then d[v] = d[u] + w(u,v); parent[v] = u`**. Yani daha kısa bir yol bulunursa `v`'nin mesafesi güncellenir ve `v`'nin **öncülü (predecessor)** `u` olarak işaretlenir (yolun geri izlenmesi için)."),
 ("Bellman-Ford hangi durumda Dijkstra yerine tercih edilmelidir?",
  "Grafikte **negatif ağırlıklı kenarlar** varsa veya **negatif çevrim tespiti** gerekiyorsa Bellman-Ford şarttır (Dijkstra yanlış sonuç verir). Ayrıca **dağıtık (distributed)** bir ortamda — örneğin distance-vector ağ yönlendirme protokollerinde — her düğüm yalnızca komşularıyla haberleşerek çalıştığı için Bellman-Ford daha uygundur. Tüm ağırlıklar pozitif ve hız önemliyse Dijkstra tercih edilir."),
 ("Bellman-Ford'un en iyi (best case) çalışma zamanı ne olabilir, neden?",
  "Eğer grafikte negatif kenar yoksa ve bir tur boyunca **hiçbir gevşetme yapılmazsa** (erken durdurma/early termination optimizasyonu ile) algoritma erken biter; bu durumda maliyet bir tam tur kenar taramasına, yani yaklaşık **O(E)**'ye (slaytta O(V) olarak ifade edilir) iner. Standart, optimizasyonsuz Bellman-Ford ise her durumda V−1 tur döner ve O(VE)'dir."),
]
})

# ===========================================================================
# L10 — Minimum Cost Spanning Tree (Prim & Kruskal)
# ===========================================================================
LECTURES.append({
"code": "L10",
"title": "Minimum Cost Spanning Tree — Prim & Kruskal",
"subtitle": "MCST tanımı, Prim's, Kruskal's, Union-Find, karşılaştırma",
"body": r"""
## MCST nedir?
**Minimum Cost Spanning Tree (MCST)**, bağlı ve ağırlıklı bir grafikte; **tüm düğümleri**
**çevrim oluşturmadan** birbirine bağlayan ve **toplam kenar ağırlığı en küçük** olan kenar
alt kümesidir. `V` düğüm için ağaçta tam olarak **V−1 kenar** vardır. Uygulamalar: ağ tasarımı,
ulaşım planlama, kaynak tahsisi.

## Prim Algoritması
**Greedy.** Keyfi bir düğümden başlar; her adımda **MCST'ye dahil olan bir düğümü, dahil
olmayan bir düğüme** bağlayan **en ucuz kenarı** ekler; tüm düğümler dahil olana kadar sürer.

```text
Prim(G):
1. mstSet = ∅; tüm key[v] = ∞; key[başlangıç] = 0; parent[başlangıç] = -1
2. while mstSet tüm düğümleri içermiyorsa:
3.     u = mstSet dışındaki en küçük key'li düğüm
4.     mstSet'e u ekle
5.     for each komşu v of u:
6.         if w(u,v) < key[v]:
7.             key[v] = w(u,v); parent[v] = u
8. return parent[]   // ağacın kenarları
```
Karmaşıklık: **O(E log V)** (binary/Fibonacci heap ile); basit dizi ile O(V²).

## Kruskal Algoritması
**Greedy.** Tüm kenarları **ağırlığa göre artan** sıraya dizer; sırayla en ucuz kenarı alır,
**çevrim oluşturmuyorsa** ekler, oluşturuyorsa atar; ağaçta **V−1 kenar** olana kadar sürer.

```text
Kruskal(G):
1. Tüm kenarları ağırlığa göre artan sırala
2. for each kenar (u,v) (artan sırada):
3.     if u ve v farklı kümelerdeyse (çevrim yok):  // Union-Find
4.         kenarı MST'ye ekle; union(u, v)
5.     // aynı kümedeyse atla (çevrim olurdu)
6. (V-1 kenara ulaşınca dur)
```
Karmaşıklık: **O(E log E)** (kenar sıralama baskın).

## Union-Find (çevrim tespiti)
Kruskal'da bir kenarın çevrim oluşturup oluşturmadığını anlamak için **Union-Find / Disjoint Set**
kullanılır:
- **Find(x):** x'in ait olduğu kümenin kökünü (temsilcisini) bulur.
- **Union(a, b):** a ve b'nin kökleri **farklıysa** kümeleri birleştirir.
Bir kenarın iki ucu **aynı kökteyse**, eklemek **çevrim** oluşturur → kenar atlanır.

## Prim vs Kruskal
- **Prim** bir düğümden büyür, **bağlı grafik** gerektirir, **yoğun (dense)** grafiklerde hızlı,
  list/priority-queue tercih eder.
- **Kruskal** en küçük kenardan başlar, **orman (forest)** üretebilir (kopuk bileşenlerde de
  çalışır), **seyrek (sparse)** grafiklerde hızlı, heap/Union-Find kullanır.

:::exam Klasik: bir grafiğin MCST'sini Prim VEYA Kruskal ile adım adım bulup toplam maliyeti
yazma; V−1 kenar kuralı; Union-Find ile çevrim tespiti; iki algoritmanın farkları.
:::
""",
"qa": [
 ("Minimum Cost Spanning Tree (MCST) nedir? V düğümlü bir grafikte kaç kenarı olur?",
  "MCST, **bağlı ve ağırlıklı** bir grafikte tüm düğümleri **çevrim oluşturmadan** bağlayan ve **toplam ağırlığı minimum** olan kenar alt kümesidir. V düğümlü bir grafikte spanning tree'nin **tam olarak V−1 kenarı** vardır (ağaç olduğu için çevrim yok, hepsi bağlı). Ağ tasarımı, ulaşım planlama, kaynak tahsisi gibi optimizasyon problemlerinde kullanılır."),
 ("Prim algoritması nasıl çalışır? Hangi paradigmaya dayanır?",
  "Prim **greedy** bir algoritmadır. **Keyfi bir başlangıç düğümünden** başlar ve her adımda, **MCST'ye dahil bir düğümü dahil olmayan bir düğüme** bağlayan **en ucuz (minimum ağırlıklı) kenarı** ekler. Tüm düğümler ağaca dahil olana kadar bu sürer. 'key' değerleri, henüz dahil olmayan düğümleri ağaca bağlayan minimum kenar ağırlığını tutar. Karmaşıklığı heap ile **O(E log V)**'dir."),
 ("Kruskal algoritması nasıl çalışır?",
  "Kruskal da **greedy**'dir. Adımları: (1) Tüm kenarları **ağırlığa göre artan** sırala. (2) En küçük kenardan başlayarak sırayla al; kenar mevcut ağaçla **çevrim oluşturmuyorsa ekle**, oluşturuyorsa **atla**. (3) Ağaçta **V−1 kenar** olana kadar devam et. Çevrim kontrolü **Union-Find** ile yapılır. Karmaşıklığı **O(E log E)**'dir (kenar sıralama baskın terim)."),
 ("Kruskal'da çevrim (cycle) tespiti için kullanılan Union-Find algoritması nasıl çalışır?",
  "**Union-Find (Disjoint Set)** düğümleri ayrık kümelerde tutar. **Find(x)** işlemi x'in ait olduğu kümenin **kökünü/temsilcisini** bulur. Bir `(u,v)` kenarı için: `Find(u)` ve `Find(v)` aynı kökü veriyorsa, u ve v **zaten aynı kümededir** → kenarı eklemek **çevrim** oluşturur, atlanır. Farklı köklerdelerse **Union(u,v)** ile iki küme birleştirilir ve kenar ağaca eklenir."),
 ("Prim ve Kruskal algoritmalarının zaman karmaşıklıkları nedir?",
  "**Prim:** basit dizi implementasyonuyla **O(V²)**, binary/Fibonacci heap ile **O(E log V)**'ye iyileştirilebilir. **Kruskal:** **O(E log E)** — baskın maliyet tüm kenarların ağırlığa göre **sıralanmasıdır** (E log E ≈ E log V). Pratikte Prim yoğun grafiklerde, Kruskal seyrek grafiklerde daha hızlıdır."),
 ("Prim ve Kruskal arasındaki temel farklar nelerdir?",
  "**Prim** keyfi bir **düğümden** başlayıp ağacı büyütür; yalnızca **bağlı grafiklerde** çalışır; her an **bağlı bir bileşen** üretir; **yoğun (dense)** grafiklerde hızlıdır; öncelik kuyruğu/liste kullanır. **Kruskal** en **düşük ağırlıklı kenardan** başlar; **kopuk bileşenlerde de** çalışır (ara adımlarda **orman/forest** üretebilir); **seyrek (sparse)** grafiklerde hızlıdır; heap ve Union-Find kullanır."),
 ("Prim ve Kruskal aynı grafikte her zaman aynı toplam ağırlığı mı verir? Aynı ağacı mı?",
  "İkisi de **aynı minimum toplam ağırlığı** garanti eder (ikisi de optimal MCST bulur). Ancak kenar ağırlıkları arasında **eşitlikler** varsa, seçilen **kenar kümesi (ağacın şekli) farklı olabilir** — birden çok geçerli MCST olabilir. Yani toplam maliyet hep aynıdır; ağacın kendisi farklı olabilir. Prim'de başlangıç düğümü seçimi de üretilen ağacı etkileyebilir."),
]
})

# ===========================================================================
# L11 — Graph Traversals (BFS & DFS)
# ===========================================================================
LECTURES.append({
"code": "L11",
"title": "Graf Gezinmeleri — BFS ve DFS",
"subtitle": "Breadth-First / Depth-First Search, queue/stack, O(V+E), uygulamalar",
"body": r"""
## Graf hatırlatma
**Graph G = (V, E)**: V düğümler (vertices), E kenarlar (edges) kümesidir. Bir kenar `(v, w)`
iki düğüm arasındaki bağlantıdır. **Degree (derece):** bir düğüme değen kenar sayısı.

## BFS — Breadth-First Search (Enine Arama)
Kök düğümden başlar; **önce tüm komşuları (aynı seviye)** ziyaret eder, sonra bir alt seviyeye
geçer. **Queue (FIFO)** ile uygulanır. **Ağırlıksız grafikte en kısa yolu (en az kenarlı)
garanti eder.**

```text
BFS(G, start):
    Q = boş queue
    Q.enqueue(start); start'ı visited işaretle
    while Q boş değil:
        y = Q.dequeue()
        process(y)
        for each komşu z of y:
            if z visited değil:
                visited işaretle; Q.enqueue(z)
```

## DFS — Depth-First Search (Derinine Arama)
Kök düğümden başlar; **bir dalı sonuna kadar** gider, sonra geri döner (backtrack). **Stack**
veya **recursion** ile uygulanır.

```cpp
void DFS(int node, vector<bool>& visited, vector<int> adj[]) {
    visited[node] = true;
    cout << node << " ";                 // process
    for (int komsu : adj[node])
        if (!visited[komsu])
            DFS(komsu, visited, adj);    // derine in (recursive)
}
```

## Karşılaştırma
| Özellik | BFS | DFS |
|---|---|---|
| Veri yapısı | Queue (FIFO) | Stack / Recursion |
| Strateji | Seviye seviye (enine) | Dala dal (derine) |
| Bellek | Daha çok (tüm seviye) | Daha az (tek yol) |
| En kısa yol (ağırlıksız) | ✅ Garanti | ❌ Garanti değil |
| Yol geri-üretimi | Zor (predecessor gerekir) | Kolay |
| En iyi kullanım | En kısa yol, web crawling | Çevrim tespiti, topolojik sıralama, bulmaca |

**Zaman karmaşıklığı (ikisi de): O(|V| + |E|)** — her düğüm ve her kenar bir kez işlenir.
`O(V·E)` değildir çünkü her kenara sadece bir kez bakılır.

## Örnek (sıralar)
İkili ağaçta: **BFS (level order)** = 1,2,3,4,5,6,7; **DFS (pre-order = Kök,Sol,Sağ)** = 1,2,4,5,3,6,7.

## Uygulamalar
- **BFS:** ağda en kısa yol, web crawling (sayfa keşfi), sosyal ağda ortak arkadaş.
- **DFS:** çevrim tespiti, topolojik sıralama, topluluk/cluster bulma, bulmaca/maze çözme.

:::exam Çok sorulur: BFS→queue/DFS→stack; ikisinin de O(V+E) olması; BFS'in (ağırlıksız) en kısa
yolu garanti etmesi; verilen graf/ağaç için BFS ve DFS ziyaret sırasını yazma.
:::
""",
"qa": [
 ("BFS ve DFS hangi veri yapılarını kullanır?",
  "**BFS, Queue (FIFO)** kullanır: ziyaret edilecek düğümler kuyruğa eklenir, baştan çıkarılır; bu yüzden graf **seviye seviye (enine)** gezilir. **DFS, Stack (LIFO)** kullanır — açıkça bir yığınla ya da **recursion** (çağrı yığını) ile; bu yüzden bir **dal sonuna kadar derine** inilir, sonra geri dönülür (backtrack)."),
 ("Hem BFS hem DFS'in zaman karmaşıklığı nedir ve neden O(V·E) değildir?",
  "İkisi de **O(|V| + |E|)**'dir: her düğüm bir kez ziyaret edilir (V) ve her kenara komşuları incelerken bir kez (yönsüzde iki kez) bakılır (E). **O(V·E) değildir** çünkü her kenar tekrar tekrar değil, **toplamda yalnızca bir kez** işlenir — düğüm başına tüm kenarları değil, sadece o düğümün komşularını tararız; bu da tüm graf için toplam E işlemdir."),
 ("BFS neden ağırlıksız bir grafikte en kısa yolu garanti eder, DFS neden etmez?",
  "BFS grafı **seviye seviye** gezer: önce 1 kenar uzaktakiler, sonra 2 kenar uzaktakiler... Bir düğüme **ilk ulaşıldığında** mutlaka **en az kenarlı (en kısa)** yolla ulaşılmıştır. DFS ise bir dalı sonuna kadar takip eder; hedefe **dolambaçlı** bir yolla erken varabilir, bu yüzden bulduğu yol en kısa olmayabilir. Örn. DFS `a→d→c→f` bulurken en kısası `a→d→f` olabilir."),
 ("BFS ve DFS'in bellek kullanımı ve yol geri-üretimi açısından farkı nedir?",
  "**Bellek:** BFS bir seviyedeki tüm komşuları kuyrukta tuttuğu için **daha çok bellek** harcar; DFS yalnızca mevcut yolu (stack) tuttuğu için **daha az bellek** kullanır. **Yol geri-üretimi:** DFS'te alınan kenar dizisini izlemek **kolaydır**; BFS birçok yolu paralel keşfettiği için yolu yeniden kurmak **zordur** — her düğümde **predecessor (öncül)** referansı saklamak gerekir."),
 ("Bir ikili ağaç için BFS (level-order) ve DFS (pre-order) ziyaret sırası nasıl olur?",
  "**BFS = level order:** kökten başlayıp **seviye seviye** soldan sağa: kök, sonra 2. seviye, sonra 3. seviye... Örn. tam ikili ağaç için `1,2,3,4,5,6,7`. **DFS pre-order = (Kök, Sol, Sağ):** önce kök, sonra sol alt ağaç (özyinelemeli), sonra sağ alt ağaç. Aynı ağaç için `1,2,4,5,3,6,7`. (DFS'in diğer biçimleri: in-order ve post-order.)"),
 ("BFS ve DFS sırasıyla hangi tür problemler için daha uygundur?",
  "**BFS:** ağırlıksız grafikte **en kısa yol**, ağ yönlendirmede mesafe, **web crawling** (bir sayfanın bağlantılarını seviye seviye keşfetme), sosyal ağda ortak arkadaş bulma. **DFS:** **çevrim tespiti**, **topolojik sıralama**, bir DAG'ı işleme, topluluk/cluster bulma, labirent/bulmaca çözme (bir yolu sonuna kadar deneyip geri dönme)."),
 ("DFS'in özyinelemeli (recursive) implementasyonunda 'visited' dizisi neden gereklidir?",
  "Graf, ağacın aksine **çevrim (cycle)** içerebilir. 'visited' işareti olmadan, çevrimli bir grafikte aynı düğümler tekrar tekrar ziyaret edilir ve DFS **sonsuz döngüye** girer. Bir düğüm ilk ziyaret edildiğinde `visited[node]=true` yapılır; komşulara inerken yalnızca **ziyaret edilmemiş** olanlar için özyinelemeye gidilir. Böylece her düğüm tam bir kez işlenir ve sonsuz döngü engellenir."),
]
})

# ===========================================================================
# L12 — Knapsack Problem
# ===========================================================================
LECTURES.append({
"code": "L12",
"title": "Knapsack (Sırt Çantası) Problemi",
"subtitle": "Fractional (greedy) vs 0/1 (dynamic programming & recursion)",
"body": r"""
## Problem tanımı
Her birinin bir **ağırlığı (weight)** ve **değeri (value)** olan nesneler ve bir **kapasitesi (W)**
olan çanta verilir. Amaç: **toplam ağırlık ≤ W** kısıtını sağlarken **toplam değeri maksimize**
etmek. İki versiyonu vardır.

## 1) Fractional Knapsack (Kesirli)
Nesneler **bölünebilir** — bir nesnenin bir kısmı alınabilir. **Greedy** ile **optimal** çözülür:
nesneleri **değer/ağırlık oranına (value/weight)** göre azalan sırala, en yüksek orandan
başlayarak doldur; son nesne sığmazsa kesrini al.

```cpp
struct Item { int value, weight; };
bool cmp(Item a, Item b) {
    return (double)a.value / a.weight > (double)b.value / b.weight;  // orana göre
}
double fractionalKnapsack(int W, Item items[], int n) {
    sort(items, items + n, cmp);
    double total = 0.0;
    for (int i = 0; i < n; i++) {
        if (items[i].weight <= W) {        // tamamı sığıyor
            W -= items[i].weight;
            total += items[i].value;
        } else {                            // kesrini al ve bitir
            total += items[i].value * ((double)W / items[i].weight);
            break;
        }
    }
    return total;
}
```

## 2) 0/1 Knapsack
Her nesne **ya tamamen alınır ya hiç** — bölünemez (binary karar). **Greedy ÇALIŞMAZ**;
**Dynamic Programming (DP)** ya da recursion ile çözülür.

:::warn Greedy (en yoğunu seç) 0/1'de yanlış sonuç verir. Örn. W=50; I1(v=60,w=10),
I2(v=100,w=20), I3(v=120,w=30). Yoğunluk sırası I1>I2>I3 ama **optimal = I2+I3 = 220**, I1 değil.
:::

### DP çözümü
`dp[i][w]` = ilk `i` nesne ve kapasite `w` ile elde edilebilecek maksimum değer.
```cpp
int knapsack01(int W, int wt[], int val[], int n) {
    int dp[n + 1][W + 1];
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;                       // taban
            else if (wt[i - 1] <= w)               // i. nesne sığıyor
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],  // al
                               dp[i - 1][w]);                          // alma
            else
                dp[i][w] = dp[i - 1][w];            // sığmıyor -> alma
        }
    }
    return dp[n][W];
}
```
Karmaşıklık: **O(n·W)** zaman ve bellek (pseudo-polynomial).

### Recursive (DP'siz) çözüm
```cpp
int knap(int W, int wt[], int val[], int n) {
    if (n == 0 || W == 0) return 0;                 // base case
    if (wt[n - 1] > W)                              // sığmıyor
        return knap(W, wt, val, n - 1);
    return max(val[n - 1] + knap(W - wt[n - 1], wt, val, n - 1),  // al
               knap(W, wt, val, n - 1));                          // alma
}
```

## Uygulamalar
Portföy optimizasyonu, kaynak tahsisi, cutting stock, sunucu/VM yerleştirme, çizelgeleme, lojistik.

:::exam Ayrım çok önemli: Fractional → greedy (value/weight) → optimal; 0/1 → DP/recursion, greedy
başarısız. DP tablosunun `max(al, alma)` mantığı ve O(nW) karmaşıklığı.
:::
""",
"qa": [
 ("Fractional Knapsack ile 0/1 Knapsack arasındaki temel fark nedir?",
  "**Fractional Knapsack**'te nesneler **bölünebilir** — bir nesnenin **kesri** (bir kısmı) alınabilir. **0/1 Knapsack**'te ise her nesne için **ikili (binary) karar** vardır: ya **tamamen al** ya da **hiç alma**; nesne bölünemez. Bu fark çözüm yöntemini belirler: fractional greedy ile, 0/1 ise DP/recursion ile çözülür."),
 ("Fractional Knapsack neden greedy ile optimal çözülür? Greedy kriteri nedir?",
  "Fractional'da nesneler bölünebildiği için, **birim ağırlık başına en değerli** nesneyi önce almak her zaman optimaldir. Greedy kriteri: nesneleri **value/weight (değer/ağırlık) oranına** göre **azalan** sırala, en yüksek oranlıdan başlayarak çantayı doldur. Son nesne tam sığmazsa, kalan kapasiteyi dolduracak **kesrini** al. Bölünebilirlik, greedy seçimi optimal yapar."),
 ("0/1 Knapsack'i greedy (en yüksek value/weight) ile çözmeye çalışırsak neden başarısız olur? Örnek verin.",
  "Çünkü nesneler bölünemez; en yoğun nesneyi almak kalan kapasiteyi **boşa harcayabilir**. Slayt örneği: W=50; I1(v=60,w=10, yoğunluk 6), I2(v=100,w=20, yoğunluk 5), I3(v=120,w=30, yoğunluk 4). Greedy önce I1'i alır, sonra I2'yi → 60+100=160, kapasite 20 boşa gider. Oysa **optimal I2+I3 = 220**'dir. Greedy 0/1'de yanlış sonuç verir; **DP** gerekir."),
 ("0/1 Knapsack DP tablosunda `dp[i][w]` ne anlama gelir ve nasıl doldurulur?",
  "`dp[i][w]` = **ilk i nesne** kullanılarak ve **kapasite w** ile elde edilebilecek **maksimum değer**. Doldurma: i. nesne sığmıyorsa (`wt[i-1] > w`) onu **alamayız** → `dp[i][w] = dp[i-1][w]`. Sığıyorsa **iki seçeneğin maksimumu** alınır: **alma** (`dp[i-1][w]`) veya **al** (`val[i-1] + dp[i-1][w - wt[i-1]]`). Taban: `i=0` veya `w=0` → `dp=0`."),
 ("0/1 Knapsack'in DP çözümünün zaman ve uzay karmaşıklığı nedir?",
  "DP tablosu `(n+1) × (W+1)` boyutundadır ve her hücre O(1) sürede doldurulur. Dolayısıyla hem **zaman hem uzay O(n·W)**'dir. Buna **pseudo-polynomial** denir çünkü karmaşıklık nesne sayısı n'e ve kapasite **W'nin değerine** bağlıdır (W'nin bit uzunluğuna değil). W çok büyükse bu maliyet ciddi olabilir."),
 ("0/1 Knapsack'in recursive çözümündeki base case ve iki seçenek nedir?",
  "**Base case:** `n == 0 || W == 0` → 0 (nesne kalmadı ya da kapasite bitti, değer 0). Her nesne için: eğer **sığmıyorsa** (`wt[n-1] > W`) onu atlayıp `knap(W, ..., n-1)` çağrılır. Sığıyorsa **iki seçeneğin max'ı** alınır: nesneyi **al** (`val[n-1] + knap(W - wt[n-1], ..., n-1)`) ya da **alma** (`knap(W, ..., n-1)`). Bu iki dallı 'al/alma' yapısı problemin özüdür."),
 ("Knapsack probleminin gerçek dünya uygulamalarına üç örnek verin.",
  "**Portföy optimizasyonu** (sınırlı bütçeyle en yüksek getirili yatırım kombinasyonunu seçme), **kaynak tahsisi** (sınırlı zaman/işgücü/ekipmanı en yüksek faydalı görevlere dağıtma), **cutting stock** (ham malzemeyi minimum fire ile kesme). Ayrıca **bulut bilişimde VM/konteyner yerleştirme**, **çizelgeleme/zaman yönetimi** ve **lojistik/araç yükleme** de Knapsack'in uygulama alanlarıdır."),
]
})

# ===========================================================================
# L13 — Topological Sorting (Kahn's Algorithm)
# ===========================================================================
LECTURES.append({
"code": "L13",
"title": "Topolojik Sıralama — Kahn Algoritması",
"subtitle": "DAG, in-degree, BFS tabanlı sıralama, çevrim tespiti, O(V+E)",
"body": r"""
## Topolojik sıralama nedir?
Bir **Directed Acyclic Graph (DAG)** için topolojik sıralama, düğümlerin öyle bir **doğrusal
sıralamasıdır** ki, **her yönlü `u → v` kenarı için `u`, `v`'den önce gelir.**
- **Bağımlılık çözümü** (dependency resolution): kısıtlı görev çizelgeleme için şarttır.
- **Sadece DAG'lar için:** **çevrim (cycle) varsa** topolojik sıralama **imkânsızdır**.
- **Birden çok geçerli sıralama** olabilir.

## In-degree (giriş derecesi) kavramı
Bir düğümün **in-degree**'si, ona **gelen (yönlü) kenar sayısıdır** — yani o düğümün **çözülmesi
gereken bağımlılık sayısı**. **In-degree = 0** olan düğümün bağımlılığı yoktur; **başlangıç
noktasıdır**. Bir düğümü işleyince, çıkan kenarları "kaldırırız" → komşularının in-degree'si azalır.

## Kahn Algoritması (BFS tabanlı)
```text
1. Compute:    Her düğümün in-degree'sini hesapla (tüm komşuluk listelerini gez)
2. Initialize: in-degree = 0 olan tüm düğümleri Queue'ya koy
3. Process:    Queue boş olmadıkça:
                 - düğümü çıkar (pop), sonuç listesine ekle
                 - her komşusunun in-degree'sini 1 azalt
                 - in-degree'si 0 olan komşuyu Queue'ya ekle
```

```cpp
vector<int> topoSort(int V, vector<int> adj[]) {
    vector<int> indeg(V, 0), result;
    for (int u = 0; u < V; u++)
        for (int v : adj[u]) indeg[v]++;        // in-degree hesapla

    queue<int> q;
    for (int i = 0; i < V; i++)
        if (indeg[i] == 0) q.push(i);           // 0 olanları kuyruğa al

    while (!q.empty()) {
        int u = q.front(); q.pop();
        result.push_back(u);                     // sıraya ekle
        for (int v : adj[u])
            if (--indeg[v] == 0) q.push(v);      // bağımlılığı çözülen komşu
    }
    return result;
}
```

## Çevrim tespiti (built-in)
Kahn'ın güçlü yanı: sıralama sonunda **`result.size() != V`** ise grafikte **çevrim** vardır.
```cpp
if (result.size() != V) return "Graf çevrim içeriyor!";
```
Sebep: bir çevrimdeki her düğümün **en az bir çözülemeyen bağımlılığı** vardır → in-degree'leri
hiçbir zaman 0 olmaz → kuyruğa hiç girmezler → sonuca eklenmezler.

## Karmaşıklık
- **Zaman: O(V + E)** — her düğüm bir kez kuyruğa girer/çıkar (V), her kenar in-degree azaltmak
  için bir kez gezilir (E).
- **Uzay: O(V)** — in-degree dizisi, kuyruk ve sonuç vektörü.

## Örnek
Düğümler 0–5; kenarlar: 5→2, 5→0, 4→0, 4→1, 2→3, 3→1. Başta in-degree=0 olanlar: **4 ve 5**.
Geçerli bir topolojik sıra: **4, 5, 2, 0, 3, 1**.

:::exam Mutlaka: topolojik sıralama sadece DAG'da; in-degree=0'dan başlama; Kahn BFS-tabanlı +
queue; çevrim tespiti `result.size() != V`; O(V+E). Verilen graf için in-degree tablosu + sıra çıkarma.
:::
""",
"qa": [
 ("Topolojik sıralama nedir ve hangi tür grafiklerde yapılabilir?",
  "Topolojik sıralama, bir **Directed Acyclic Graph (DAG)**'ın düğümlerinin öyle bir **doğrusal sıralamasıdır** ki, **her yönlü `u → v` kenarı için u her zaman v'den önce gelir**. Yalnızca **çevrimsiz yönlü grafiklerde (DAG)** mümkündür; grafikte bir **çevrim (cycle)** varsa topolojik sıralama **imkânsızdır** (karşılıklı bağımlılık olur). Bir grafın **birden fazla** geçerli topolojik sıralaması olabilir."),
 ("Bir düğümün 'in-degree' (giriş derecesi) değeri neyi temsil eder?",
  "**In-degree**, bir düğüme **gelen yönlü kenarların sayısıdır**. Bağımlılık (dependency) bağlamında, o düğümün **işlenebilmesi için önce çözülmesi gereken bağımlılık sayısını** temsil eder. **In-degree = 0** olan bir düğümün hiçbir bağımlılığı yoktur, bu yüzden topolojik sıralamada bir **başlangıç noktası** olabilir."),
 ("Kahn algoritmasının üç ana adımı nedir?",
  "(1) **Compute:** Tüm komşuluk listeleri gezilerek her düğümün **in-degree**'si hesaplanır. (2) **Initialize:** **In-degree = 0** olan tüm düğümler bir **kuyruğa (queue)** eklenir. (3) **Process:** Kuyruk boşalana kadar: bir düğüm çıkarılır ve **sonuç listesine** eklenir; çıkan düğümün her komşusunun in-degree'si **1 azaltılır**; in-degree'si **0'a düşen** komşu kuyruğa eklenir. Kahn **BFS tabanlıdır** (queue kullanır)."),
 ("Kahn algoritması bir grafikteki çevrimi (cycle) nasıl tespit eder?",
  "Algoritma bittiğinde **sonuç listesinin boyutu düğüm sayısına eşit değilse** (`result.size() != V`) grafikte **çevrim** vardır. Sebep: bir çevrime dahil her düğümün, kaynağı yine çevrimdeki başka bir düğüm olan **çözülemeyen** en az bir bağımlılığı (gelen kenarı) vardır; bu yüzden in-degree'leri **asla 0'a düşmez**, kuyruğa hiç girmezler ve sonuç listesine eklenmezler. Eksik düğümler çevrimi gösterir."),
 ("Kahn algoritmasının zaman ve uzay karmaşıklığı nedir?",
  "**Zaman: O(V + E)** — her düğüm tam bir kez kuyruğa eklenir ve çıkarılır (V), ve her kenar, komşunun in-degree'sini azaltmak için tam bir kez gezilir (E). **Uzay: O(V)** — in-degree dizisi, kuyruk (queue) ve sonuç (result) vektörü düğüm sayısı kadar yer tutar. Bu, BFS'in karmaşıklığıyla aynıdır."),
 ("Kahn algoritmasında neden başlangıçta in-degree = 0 olan düğümler kuyruğa eklenir?",
  "Çünkü **in-degree = 0** olan düğümlerin **hiçbir bağımlılığı yoktur** — onları işlemeden önce çözülmesi gereken bir önceki düğüm bulunmaz. Dolayısıyla topolojik sıralamada **en başta** gelebilirler ve güvenle işlenebilirler. Bir düğüm işlenince çıkan kenarları kaldırılır, komşularının in-degree'si azalır ve sırası gelen yeni '0' düğümler kuyruğa katılır."),
 ("Düğümleri 0–5 olan ve kenarları 5→2, 5→0, 4→0, 4→1, 2→3, 3→1 olan graf için geçerli bir topolojik sıra üretin.",
  "Önce in-degree'ler: 0←(4,5)=2, 1←(4,3)=2, 2←(5)=1, 3←(2)=1, 4=0, 5=0. Başlangıç kuyruğu: **{4, 5}**. 4 çıkar → 0 ve 1'in in-degree'si azalır (0→1, 1→1). 5 çıkar → 2 ve 0 azalır (2→0, 0→0); kuyruğa 2 ve 0 girer. Sırayla 2 çıkar → 3→0 (kuyruğa); 0 çıkar (komşusu yok); 3 çıkar → 1→0 (kuyruğa); 1 çıkar. Sonuç: **4, 5, 2, 0, 3, 1**. (Geçerli başka sıralar da vardır.)"),
]
})

print("ALL lectures loaded:", len(LECTURES))


