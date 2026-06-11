# -*- coding: utf-8 -*-
# Klasik sorular: kod boşluk doldurmaca. prompt = boşluklu kod, answer = çözüm.

CLASSIC = []

CLASSIC.append({
"topic":"L3 · Recursion — Factorial",
"prompt": r"""
Aşağıdaki özyinelemeli `factorial` fonksiyonundaki boşlukları doldurun.

```cpp
int factorial(int n) {
    if (n <= 1)
        return ____;                 // (1) base case dönüş değeri
    return n * factorial(____);      // (2) özyinelemeli çağrı argümanı
}
```
""",
"answer": r"""
**(1) → `1`**  ·  **(2) → `n - 1`**

```cpp
int factorial(int n) {
    if (n <= 1)
        return 1;                    // base case: 0! = 1! = 1
    return n * factorial(n - 1);     // n! = n * (n-1)!
}
```
Base case olmadan (veya argüman küçülmezse) sonsuz özyineleme olur. `n` her çağrıda 1 azalarak base case'e ilerler.
"""
})

CLASSIC.append({
"topic":"L3 · Recursion — Euclid GCD",
"prompt": r"""
Euclid'in en büyük ortak bölen (GCD) fonksiyonunu tamamlayın.

```cpp
int gcd(int u, int v) {
    if (____)                        // (1) base case koşulu
        return u;
    return gcd(v, ____);             // (2) ikinci argüman
}
```
""",
"answer": r"""
**(1) → `v == 0`**  ·  **(2) → `u % v`**

```cpp
int gcd(int u, int v) {
    if (v == 0)
        return u;                    // bölen 0 ise sonuç u
    return gcd(v, u % v);            // gcd(u,v) = gcd(v, u mod v)
}
```
Her adımda ikinci argüman `u % v` ile küçülür ve eninde sonunda `v == 0` base case'ine ulaşılır.
"""
})

CLASSIC.append({
"topic":"L3/L5 · Selection Sort",
"prompt": r"""
Selection Sort'taki eksik satırları doldurun (artan sıralama).

```cpp
void selectionSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int small = i;
        for (int j = ____; j < n; j++)     // (1) iç döngü başlangıcı
            if (A[j] ____ A[small])         // (2) karşılaştırma operatörü
                small = j;
        int temp = A[small];                // swap A[i] <-> A[small]
        A[small] = A[i];
        A[i] = ____;                         // (3)
    }
}
```
""",
"answer": r"""
**(1) → `i + 1`**  ·  **(2) → `<`**  ·  **(3) → `temp`**

```cpp
for (int j = i + 1; j < n; j++)   // i'den sonrasında en küçüğü ara
    if (A[j] < A[small])           // daha küçük bulundu
        small = j;
int temp = A[small];
A[small] = A[i];
A[i] = temp;                       // takas tamamlandı
```
İç döngü `i+1`'den başlar çünkü `A[i]` zaten aday (small=i) olarak alınmıştır. `<` operatörü artan sıralama verir.
"""
})

CLASSIC.append({
"topic":"L5 · Bubble Sort",
"prompt": r"""
Bubble Sort'un iç döngüsünü ve takas koşulunu tamamlayın.

```cpp
void bubbleSort(int A[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < ____; j++)     // (1) iç döngü sınırı
            if (A[j] ____ A[j + 1]) {        // (2) komşu karşılaştırma
                int t = A[j];
                A[j] = A[j + 1];
                A[j + 1] = ____;             // (3)
            }
}
```
""",
"answer": r"""
**(1) → `n - 1 - i`**  ·  **(2) → `>`**  ·  **(3) → `t`**

```cpp
for (int j = 0; j < n - 1 - i; j++)   // her turda son i eleman yerine oturmuştur
    if (A[j] > A[j + 1]) {              // komşular ters sırada
        int t = A[j];
        A[j] = A[j + 1];
        A[j + 1] = t;                  // swap
    }
```
`n-1-i` sınırı, her dış turda en büyük elemanın sona oturduğunu ve tekrar kontrol edilmesine gerek olmadığını kullanır.
"""
})

CLASSIC.append({
"topic":"L5 · Insertion Sort",
"prompt": r"""
Insertion Sort'taki kaydırma (shift) mantığını tamamlayın.

```cpp
void insertionSort(int A[], int n) {
    for (int i = 1; i < n; i++) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > ____) {   // (1) karşılaştırılan değer
            A[j + 1] = A[j];               // büyük elemanı sağa kaydır
            j____;                          // (2) j güncelleme
        }
        A[____] = key;                      // (3) key'in yerleştirileceği index
    }
}
```
""",
"answer": r"""
**(1) → `key`**  ·  **(2) → `--`**  ·  **(3) → `j + 1`**

```cpp
while (j >= 0 && A[j] > key) {   // key'den büyük olanları
    A[j + 1] = A[j];             // bir sağa kaydır
    j--;                         // sola ilerle
}
A[j + 1] = key;                  // key boşalan doğru yere oturur
```
Döngü `key`'den büyük tüm elemanları sağa kaydırır; durduğunda `j+1` indexi key için doğru (sıralı) konumdur.
"""
})

CLASSIC.append({
"topic":"L2 · Linked List — Başa Ekleme",
"prompt": r"""
Bağlı listenin başına node ekleyen fonksiyonu tamamlayın.

```cpp
void addFirst(Node*& head, int deger) {
    Node* yeni = new Node();
    yeni->data = deger;
    yeni->next = ____;        // (1) yeni node neyi göstermeli?
    head = ____;              // (2) head ne olmalı?
}
```
""",
"answer": r"""
**(1) → `head`**  ·  **(2) → `yeni`**

```cpp
yeni->next = head;   // önce: yeni node eski başı gösterir
head = yeni;          // sonra: head yeni node'a taşınır
```
**Sıra kritiktir.** Önce `head = yeni` yapılırsa eski listeye olan tek bağlantı kaybolur (memory leak). Bu işlem O(1)'dir.
"""
})

CLASSIC.append({
"topic":"L2 · Linked List — Arama",
"prompt": r"""
Bağlı listede değer arayan fonksiyonu tamamlayın.

```cpp
bool search(Node* head, int aranan) {
    Node* p = head;
    while (p != ____) {            // (1) döngü koşulu
        if (p->data == aranan)
            return true;
        p = ____;                  // (2) ilerleme
    }
    return false;
}
```
""",
"answer": r"""
**(1) → `NULL`**  ·  **(2) → `p->next`**

```cpp
while (p != NULL) {       // liste sonuna kadar
    if (p->data == aranan) return true;
    p = p->next;          // bir sonraki node'a geç
}
return false;
```
Liste baştan sona gezilir (traverse). En kötü durumda tüm liste taranır → **O(n)**. Linked list'te rastgele erişim olmadığı için ikili arama yapılamaz.
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

`sum++` toplam `n²` kez çalışır (dış döngü n, iç döngü her seferinde n). Sabit başlangıç işlemleriyle birlikte:
**T(n) ≈ n² + 1  →  Big-O = O(n²)** (karesel).

İç içe döngülerde karmaşıklıklar **çarpılır**. Eğer iç döngü `j < i` olsaydı toplam `Σi = n(n-1)/2` olur ama yine **O(n²)** kalırdı.
"""
})

print("CLASSIC loaded:", len(CLASSIC))
