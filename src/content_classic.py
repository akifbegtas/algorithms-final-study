# -*- coding: utf-8 -*-
# Klasik sorular: kod boşluk doldurmaca. prompt = boşluklu kod, answer = çözüm.

CLASSIC = []

CLASSIC.append({
"topic":"L1 · OMNeT++ — TicToc temel modül",
"prompt": r"""
Temel TicToc modülündeki boşlukları doldurun.

```cpp
void Txc1::initialize() {
    if (strcmp("tic", getName()) == 0) {     // sadece tic başlatır
        cMessage *msg = new cMessage("tictocMsg");
        ____(msg, "out");                     // (1) mesajı kapıdan yollayan fonksiyon
    }
}
void Txc1::handleMessage(cMessage *msg) {
    send(msg, ____);                          // (2) hangi kapıdan geri gönderilir?
}
```
""",
"answer": r"""
**(1) → `send`**  ·  **(2) → `"out"`**

```cpp
void Txc1::initialize() {
    if (strcmp("tic", getName()) == 0) {
        cMessage *msg = new cMessage("tictocMsg");
        send(msg, "out");          // mesajı 'out' kapısından gönder
    }
}
void Txc1::handleMessage(cMessage *msg) {
    send(msg, "out");              // gelen mesajı geri yolla (ping-pong)
}
```
`initialize()` sadece bir kez (başta) çalışır ve yalnızca `tic` ilk mesajı üretir. `handleMessage()` her mesaj gelişinde çağrılır ve mesajı geri gönderir.
"""
})

CLASSIC.append({
"topic":"L2 · OMNeT++ — State variable (counter)",
"prompt": r"""
Sayaç (counter) ile simülasyonu durduran kodu tamamlayın.

```cpp
void Txc::initialize() {
    counter = ____;                  // (1) başlangıç değeri
    WATCH(counter);
    if (strcmp("tic", getName()) == 0)
        scheduleAt(0.0, new cMessage("tictocMsg"));
}
void Txc::handleMessage(cMessage *msg) {
    counter____;                      // (2) her mesajda azalt
    if (counter == 0)
        ____ msg;                     // (3) mesajı yok et -> akış dursun
    else
        send(msg, "out");
}
```
""",
"answer": r"""
**(1) → `10`**  ·  **(2) → `--`**  ·  **(3) → `delete`**

```cpp
counter = 10;        // initialize()'da başlangıç
...
counter--;           // her mesaj gelişinde azalt
if (counter == 0)
    delete msg;      // mesajı sil -> yeni olay üretilmez -> simülasyon durur
else
    send(msg, "out");
```
`WATCH(counter)` counter'ı GUI'de izlenebilir yapar. Mesaj silinmezse ping-pong sonsuza dek sürer.
"""
})

CLASSIC.append({
"topic":"L2 · OMNeT++ — Processing delay (self-message)",
"prompt": r"""
İşlem gecikmesini self-message ile modelleyen kodu tamamlayın.

```cpp
void Txc::handleMessage(cMessage *msg) {
    if (msg ____ event) {                       // (1) gelen self-message mi?
        send(message, "out");                   // bekleyen mesajı gönder
    } else {
        message = msg;                          // gelen mesajı sakla
        ____(simTime() + delayTime, event);     // (2) gecikme sonrası planla
    }
}
```
""",
"answer": r"""
**(1) → `==`**  ·  **(2) → `scheduleAt`**

```cpp
if (msg == event) {                       // self-message (timer) ateşlendi
    send(message, "out");                 // bekleyen mesajı şimdi gönder
} else {
    message = msg;
    scheduleAt(simTime() + delayTime, event);   // delayTime kadar gecikme planla
}
```
`scheduleAt` modülün **kendine** gelecekteki bir an için mesaj planlar (self-message). Böylece mesaj hemen değil, `delayTime` gecikmeyle işlenir. Timer `cancelEvent(event)` ile iptal edilebilir.
"""
})

CLASSIC.append({
"topic":"L3 · OMNeT++ — check_and_cast + yönlendirme",
"prompt": r"""
Çok düğümlü ağda mesaj yönlendiren kodu tamamlayın.

```cpp
void Txc::handleMessage(cMessage *msg) {
    TicTocMsg *ttmsg = ____<TicTocMsg *>(msg);     // (1) güvenli tür dönüşümü
    if (ttmsg->getDestination() == getIndex()) {
        EV << "Mesaj hedefe ulasti.\n";
        delete ttmsg;
    } else {
        int n = gateSize("gate");
        int k = ____(0, n - 1);                    // (2) rastgele komşu kapı seç
        send(ttmsg, "gate$o", k);                   // ilet (forward)
    }
}
```
""",
"answer": r"""
**(1) → `check_and_cast`**  ·  **(2) → `intuniform`**

```cpp
TicTocMsg *ttmsg = check_and_cast<TicTocMsg *>(msg);   // tür yanlışsa hata fırlatır
...
int k = intuniform(0, n - 1);    // 0..n-1 arası rastgele tamsayı (kapı index'i)
send(ttmsg, "gate$o", k);        // mesajı seçilen kapıdan ilet
```
`check_and_cast`, başarısız dönüşümde sessizce `nullptr` vermek yerine **açık hata** fırlatır. `intuniform(a,b)` OMNeT++'ın rastgele tamsayı üretecidir; mesaj hedefe ulaşana dek rastgele komşuya iletilir.
"""
})

CLASSIC.append({
"topic":"L4 · Greedy — Genel yapı (sözde kod)",
"prompt": r"""
Greedy method'un genel iskeletini tamamlayın.

```text
Greedy(C):                       // C = aday kümesi
    S = ____                     // (1) başlangıç çözümü
    while C boş değil:
        x = Select(C)            // locally optimal adayı seç
        C = C - {x}
        if ____(S ∪ {x}):        // (2) ekleyince kısıt sağlanıyor mu?
            S = S ∪ {x}
    return S
```
""",
"answer": r"""
**(1) → `∅` (boş küme)**  ·  **(2) → `Feasible` (uygunluk kontrolü)**

```text
S = ∅                          // çözüm boş başlar
while C boş değil:
    x = Select(C)              // her adımda yerel en iyi aday
    C = C - {x}
    if Feasible(S ∪ {x}):      // adayı eklemek kısıtı bozmuyorsa
        S = S ∪ {x}            // çözüme ekle
return S
```
Greedy her adımda **locally optimal** seçim yapar; yalnızca **feasible (uygun)** adaylar çözüme eklenir. Bu yerel seçimlerin global optimuma götürmesi **garanti değildir** (örn. 0/1 Knapsack'te başarısız olur).
"""
})

CLASSIC.append({
"topic":"L5 · Big O — Sadeleştirme",
"prompt": r"""
Aşağıdaki ifadeleri Big O kurallarıyla sadeleştirin.

```text
(1) O(2n + 3)        = ____
(2) O(n² + n)         = ____
(3) O(3n³ + 100n²)    = ____
```
Kural: sabitleri at, en yüksek dereceli terimi tut.
""",
"answer": r"""
**(1) → `O(n)`**  ·  **(2) → `O(n²)`**  ·  **(3) → `O(n³)`**

```text
O(2n + 3)       -> O(n)     // 2 katsayısı ve +3 sabiti atılır
O(n² + n)       -> O(n²)    // en yüksek dereceli terim kalır
O(3n³ + 100n²)  -> O(n³)    // 3 katsayısı atılır, en yüksek derece n³
```
İki temel kural: **(a) sabit katsayılar/toplananlar atılır**, **(b) yalnızca en yüksek dereceli terim tutulur**. n büyüdükçe baskın terim sonucu belirler.
"""
})

CLASSIC.append({
"topic":"L5 · Big O — Kod parçasının karmaşıklığı",
"prompt": r"""
Aşağıdaki kodun toplam Big O karmaşıklığını belirleyin (boşlukları doldurun).

```cpp
for (int i = 0; i < n; i++)        // ____ kez   (A)
    for (int j = 0; j < n; j++)    // her i için ____ kez   (B)
        x++;                       // alt toplam: ____   (C)

for (int k = 0; k < n; k++)        // + ____ kez   (D)
    y++;
```
Toplam Big O = ?
""",
"answer": r"""
**(A) → n**  ·  **(B) → n**  ·  **(C) → n²**  ·  **(D) → n**

İlk blok iç içe iki döngü: `n × n = n²`. İkinci blok ayrı tek döngü: `n`. Toplam `T(n) ≈ n² + n`.

```text
n² + n   --(en yüksek dereceli terim)-->   O(n²)
```
**Toplam Big O = O(n²)**. İç içe döngülerde karmaşıklıklar **çarpılır** (n²), peş peşe bloklarda **toplanır** (n²+n), ama Big O'da en büyük terim baskındır.
"""
})

# ===================== L6-L13 (değişmeden korunan klasik sorular) =====================

CLASSIC.append({
"topic":"L6 · T(n) Analizi",
"prompt": r"""
Aşağıdaki kod parçasının T(n) ve Big-O karmaşıklığını belirleyin (boşlukları doldurun).

```cpp
int sum = 0;                       // 1 kez
for (int i = 0; i < n; i++)        // ____ kez   (A)
    for (int j = 0; j < n; j++)    // her i için ____ kez   (B)
        sum++;                     // toplam: ____   (C)
```
T(n) ≈ ?  →  Big-O = ?
""",
"answer": r"""
**(A) → n**  ·  **(B) → n**  ·  **(C) → n × n = n²**

`sum++` toplam `n²` kez çalışır (dış döngü n, iç döngü her seferinde n). Sabit başlangıç işlemiyle birlikte:
**T(n) ≈ n² + 1  →  Big-O = O(n²)** (karesel).

İç içe döngülerde karmaşıklıklar **çarpılır**. Eğer iç döngü `j < i` olsaydı toplam `Σi = n(n-1)/2` olur ama yine **O(n²)** kalırdı.
"""
})

CLASSIC.append({
"topic":"L8 · Dijkstra — Relaxation",
"prompt": r"""
Dijkstra'nın gevşetme (relaxation) adımını tamamlayın.

```text
u = mesafesi en küçük olan ziyaret edilmemiş düğüm
for each komşu v of u:
    if (d[u] + c(u, v) ____ d[v])      // (1) karşılaştırma
        d[v] = ____                     // (2) yeni mesafe
```
""",
"answer": r"""
**(1) → `<`**  ·  **(2) → `d[u] + c(u, v)`**

```text
if (d[u] + c(u, v) < d[v])
    d[v] = d[u] + c(u, v)
```
"u üzerinden v'ye giden yol, v'nin bilinen mesafesinden kısa mı?" Kısaysa `d[v]` güncellenir. Dijkstra greedy olduğu için ziyaret edilen düğüm bir daha güncellenmez — bu yüzden negatif ağırlıkta çalışmaz.
"""
})

CLASSIC.append({
"topic":"L9 · Bellman-Ford",
"prompt": r"""
Bellman-Ford'un ana döngüsünü ve negatif çevrim kontrolünü tamamlayın.

```text
for i = 1 to ____ do                  // (1) kaç tur?
    for each edge (u, v) in E do
        Relax(u, v, w)

for each edge (u, v) in E do
    if d[v] > d[u] + w(u, v)
        return ____                    // (2) bu durum neyi gösterir?
```
""",
"answer": r"""
**(1) → `|V| - 1`**  ·  **(2) → `FALSE` (negatif çevrim var)**

```text
for i = 1 to |V| - 1 do        // en kısa yol en çok V-1 kenar içerir
    for each edge (u,v): Relax(u,v,w)

for each edge (u,v):           // V-1 turdan SONRA hâlâ gevşetme mümkünse
    if d[v] > d[u] + w(u,v)
        return FALSE            // negatif ağırlıklı çevrim var
```
V−1 tur tüm en kısa yolları bulmaya yeter. Sonrasında hâlâ iyileştirme yapılabiliyorsa negatif çevrim vardır. Karmaşıklık **O(V·E)**.
"""
})

CLASSIC.append({
"topic":"L11 · BFS",
"prompt": r"""
BFS'in sözde kodundaki boşlukları doldurun.

```text
BFS(G, start):
    Q = boş ____                       // (1) hangi veri yapısı?
    Q.enqueue(start); start -> visited
    while Q boş değil:
        y = Q.____()                   // (2) hangi uçtan çıkarılır?
        for each komşu z of y:
            if z visited değil:
                z -> visited
                Q.enqueue(z)
```
""",
"answer": r"""
**(1) → `queue` (FIFO)**  ·  **(2) → `dequeue` (önden çıkar)**

```text
Q = boş queue
Q.enqueue(start)
while Q boş değil:
    y = Q.dequeue()       // FIFO: ilk eklenen ilk çıkar
    ...komşuları enqueue et
```
Queue + FIFO sayesinde graf **seviye seviye** gezilir; bu yüzden BFS ağırlıksız grafikte en kısa (en az kenarlı) yolu garanti eder. Karmaşıklık **O(V+E)**.
"""
})

CLASSIC.append({
"topic":"L11 · DFS",
"prompt": r"""
Özyinelemeli DFS fonksiyonunu tamamlayın.

```cpp
void DFS(int node, vector<bool>& visited, vector<int> adj[]) {
    visited[node] = ____;                  // (1)
    cout << node << " ";
    for (int komsu : adj[node])
        if (____)                          // (2) hangi komşuya inilir?
            DFS(komsu, visited, adj);
}
```
""",
"answer": r"""
**(1) → `true`**  ·  **(2) → `!visited[komsu]`**

```cpp
visited[node] = true;                 // ziyaret edildi
for (int komsu : adj[node])
    if (!visited[komsu])              // sadece ziyaret edilmemişlere
        DFS(komsu, visited, adj);     // derine in (recursion = stack)
```
`visited` kontrolü olmadan çevrimli grafikte DFS sonsuz döngüye girer. DFS recursion (çağrı yığını = stack) ile bir dalı sonuna kadar gezer. Karmaşıklık **O(V+E)**.
"""
})

CLASSIC.append({
"topic":"L12 · 0/1 Knapsack (DP)",
"prompt": r"""
0/1 Knapsack DP geçiş (transition) satırını tamamlayın.

```cpp
if (wt[i - 1] <= w)                      // i. nesne sığıyor
    dp[i][w] = max( val[i-1] + dp[i-1][ ____ ],   // (1) AL
                    dp[____][w] );                 // (2) ALMA
else
    dp[i][w] = dp[i - 1][w];             // sığmıyor
```
""",
"answer": r"""
**(1) → `w - wt[i-1]`**  ·  **(2) → `i - 1`**

```cpp
dp[i][w] = max( val[i-1] + dp[i-1][w - wt[i-1]],  // nesneyi AL: değeri ekle,
                                                  //   kalan kapasiteye bak
                dp[i-1][w] );                     // nesneyi ALMA
```
Her nesne için **al / alma** kararının maksimumu alınır. Aldıysak kapasiteden `wt[i-1]` düşülür. Karmaşıklık **O(n·W)**. Greedy 0/1'de çalışmaz, bu yüzden DP gerekir.
"""
})

CLASSIC.append({
"topic":"L13 · Topological Sort (Kahn)",
"prompt": r"""
Kahn algoritmasındaki in-degree işlemini tamamlayın.

```cpp
// 0 in-degree'lileri kuyruğa al
for (int i = 0; i < V; i++)
    if (indeg[i] == ____) q.push(i);     // (1)

while (!q.empty()) {
    int u = q.front(); q.pop();
    result.push_back(u);
    for (int v : adj[u])
        if (____ == 0) q.push(v);         // (2) hangi koşulla v kuyruğa girer?
}
```
""",
"answer": r"""
**(1) → `0`**  ·  **(2) → `--indeg[v]`**

```cpp
for (int i = 0; i < V; i++)
    if (indeg[i] == 0) q.push(i);    // bağımlılığı olmayan düğümler başlangıç

while (!q.empty()) {
    int u = q.front(); q.pop();
    result.push_back(u);
    for (int v : adj[u])
        if (--indeg[v] == 0)         // v'nin bağımlılığı çözüldüyse
            q.push(v);
}
```
`--indeg[v]` komşunun in-degree'sini önce azaltır, 0 olduysa (tüm bağımlılıkları bitti) kuyruğa ekler. Sonda `result.size() != V` ise **çevrim** vardır. Karmaşıklık **O(V+E)**.
"""
})

print("CLASSIC loaded:", len(CLASSIC))
