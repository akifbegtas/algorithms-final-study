# -*- coding: utf-8 -*-
# 30 çoktan seçmeli soru. correct = doğru şıkkın index'i (0=A,1=B,2=C,3=D)

MCQ = [
 # --- L1 ---
 {"topic":"L1 · C++","q":"`using namespace std;` satırının temel amacı nedir?",
  "options":["Programı daha hızlı çalıştırmak","`std::` ön ekini yazmadan standart kütüphane isimlerini kullanmak ve isim çakışmalarını yönetmek","Bellekten dizi ayırmak","Dosya okuma/yazma açmak"],
  "correct":1,"explain":"namespace isimleri gruplar; `using namespace std;` std içindeki cout, cin gibi isimleri çıplak kullanmamızı sağlar ve name collision'ı önler."},
 {"topic":"L1 · C++","q":"`int a[5];` dizisinde geçerli en büyük index hangisidir?",
  "options":["5","4","6","Diziler 1'den başlar, yani 5"],
  "correct":1,"explain":"C++ dizileri 0-tabanlıdır; 5 elemanlı dizide index'ler 0..4'tür, en büyük geçerli index 4'tür. a[5] sınır dışıdır."},

 # --- L2 ---
 {"topic":"L2 · Linked List","q":"Singly linked list'te bir node hangi iki parçadan oluşur?",
  "options":["data ve index","value ve uzunluk","data ve sonraki node'a pointer (next)","key ve hash"],
  "correct":2,"explain":"Her node bir veri (data) ve bir sonraki node'un adresini tutan pointer (next) içerir; son node'un next'i NULL'dur."},
 {"topic":"L2 · Linked List","q":"Aşağıdakilerden hangisi LIFO (Last In First Out) prensibiyle çalışır?",
  "options":["Queue","Stack","Linked List","Array"],
  "correct":1,"explain":"Stack LIFO'dur (son giren ilk çıkar). Queue ise FIFO'dur (ilk giren ilk çıkar)."},

 # --- L3 ---
 {"topic":"L3 · Recursion","q":"Özyinelemeli bir fonksiyonda 'base case' (temel durum) bulunmazsa ne olur?",
  "options":["Fonksiyon daha hızlı çalışır","Sonsuz özyineleme olur ve stack taşar (stack overflow)","Derleyici hatası verir","Sonuç her zaman 0 döner"],
  "correct":1,"explain":"Base case özyinelemeyi durduran koşuldur; olmazsa çağrılar sonsuza dek devam eder ve stack overflow oluşur."},
 {"topic":"L3 · GCD","q":"Euclid algoritmasına göre `gcd(20, 12)` kaçtır?",
  "options":["2","6","4","12"],
  "correct":2,"explain":"gcd(20,12)=gcd(12,20%12=8)=gcd(8,12%8=4)=gcd(4,8%4=0)=4. Sonuç 4."},
 {"topic":"L3 · Selection Sort","q":"Selection Sort'un her durumdaki (best/average/worst) zaman karmaşıklığı nedir?",
  "options":["O(n)","O(n log n)","O(n²)","Best'te O(n), worst'te O(n²)"],
  "correct":2,"explain":"Selection sort en küçüğü bulmak için her zaman tüm sırasız kısmı tarar; girdi sıralı olsa bile Θ(n²)'dir."},

 # --- L4 ---
 {"topic":"L4 · Big O","q":"Big-Θ (theta) notasyonu hangi durumu tanımlar?",
  "options":["Sadece üst sınır (worst case)","Sadece alt sınır (best case)","Hem üst hem alt sınır (sıkı/average)","Bellek kullanımı"],
  "correct":2,"explain":"Θ hem O (üst) hem Ω (alt) sınırını birlikte sağlar; fonksiyon iki sabit katı arasında sıkışır → sıkı sınır."},
 {"topic":"L4 · Big O","q":"`f(n) = 2n⁷ − 6n⁵ + 10n² − 5` ifadesi neyin Big-O'sudur?",
  "options":["O(n²)","O(n⁵)","O(n⁷)","O(2ⁿ)"],
  "correct":2,"explain":"Her polinom, en yüksek dereceli teriminin Big-O'sudur. En yüksek derece n⁷ → O(n⁷)."},
 {"topic":"L4 · Big O","q":"Aşağıdaki büyüme fonksiyonlarından hangisi en HIZLI büyür?",
  "options":["n log n","n²","2ⁿ","n³"],
  "correct":2,"explain":"Sıralama: 1 < log n < n < n log n < n² < n³ < 2ⁿ. Üstel 2ⁿ en hızlı büyüyendir."},

 # --- L5 ---
 {"topic":"L5 · Sorting","q":"Hangi sıralama algoritması 'adaptive'tir (neredeyse sıralı veride O(n)'e yaklaşır)?",
  "options":["Selection Sort","Insertion Sort","Her ikisi de değil","Selection ve Insertion eşit"],
  "correct":1,"explain":"Insertion sort adaptive'tir; sıralı veride eleman başına tek karşılaştırma → O(n). Selection sort her durumda O(n²)'dir."},
 {"topic":"L5 · Sorting","q":"Bubble sort komşu elemanları karşılaştırırken ters sıradaysa ne yapar?",
  "options":["Onları takas eder (swap)","Birini siler","Diziyi yeniden başlatır","Hiçbir şey yapmaz"],
  "correct":0,"explain":"Bubble sort komşu çiftleri karşılaştırır ve ters sıradalarsa takas eder; takas olmayan geçiş listenin sıralı olduğunu gösterir."},
 {"topic":"L5 · Sorting","q":"Aşağıdakilerden hangisi 'stable' (kararlı) bir sıralama DEĞİLDİR?",
  "options":["Insertion Sort","Bubble Sort","Selection Sort","Hepsi stable'dır"],
  "correct":2,"explain":"Selection sort standart hâliyle stable değildir; uzak takaslar eşit anahtarların göreli sırasını bozabilir."},

 # --- L6 ---
 {"topic":"L6 · T(n)","q":"`for(i=0;i<n;i++) for(j=0;j<n;j++) x++;` kodunun T(n) karmaşıklığı nedir?",
  "options":["O(n)","O(n²)","O(log n)","O(n³)"],
  "correct":1,"explain":"İç içe iki döngü, her biri n kez → n×n = O(n²). İç içe döngülerde karmaşıklıklar çarpılır."},
 {"topic":"L6 · T(n)","q":"`for(i=n; i>1; i=i/2) x++;` döngüsünün karmaşıklığı nedir?",
  "options":["O(n)","O(n²)","O(log n)","O(1)"],
  "correct":2,"explain":"i her adımda yarıya iner (n→n/2→...→1), yaklaşık log₂n adım. Yarıya bölme → O(log n)."},

 # --- L7 ---
 {"topic":"L7 · Pandas","q":"Pandas'ta null (boş) içeren satırları silmek için hangi metot kullanılır?",
  "options":["fillna()","dropna()","drop_duplicates()","head()"],
  "correct":1,"explain":"dropna() null içeren satırları kaldırır. fillna() boşlukları bir değerle doldurur, drop_duplicates() duplike satırları siler."},
 {"topic":"L7 · Matplotlib","q":"Matplotlib'te noktaları çizgiyle bağlamadan, dağılım grafiği çizen fonksiyon hangisidir?",
  "options":["plot()","bar()","scatter()","pie()"],
  "correct":2,"explain":"scatter() her gözlem için bağımsız bir nokta çizer (dağılım). plot() varsayılan olarak noktaları çizgiyle bağlar."},

 # --- L8 ---
 {"topic":"L8 · Dijkstra","q":"Dijkstra algoritması hangi koşulda DOĞRU çalışmaz?",
  "options":["Yönlü grafiklerde","Negatif ağırlıklı kenarlar olduğunda","Çok sayıda düğüm olduğunda","Yönsüz grafiklerde"],
  "correct":1,"explain":"Dijkstra greedy'dir; ziyaret edilen düğümü kesinleştirir. Negatif kenarlar sonradan daha kısa yol yaratabileceği için yanlış sonuç verir."},
 {"topic":"L8 · Dijkstra","q":"Dijkstra hangi algoritma paradigmasını kullanır?",
  "options":["Divide and conquer","Dynamic programming","Greedy","Backtracking"],
  "correct":2,"explain":"Dijkstra greedy'dir: her adımda ziyaret edilmemiş en küçük mesafeli düğümü seçer ve kesinleştirir."},
 {"topic":"L8 · Dijkstra","q":"Dijkstra'da 'relaxation' koşulu aşağıdakilerden hangisidir?",
  "options":["if d[u] > d[v] + w(u,v)","if d[v] > d[u] + w(u,v) then d[v]=d[u]+w(u,v)","if d[v] == d[u]","if w(u,v) < 0"],
  "correct":1,"explain":"Relaxation: u üzerinden v'ye yol daha kısaysa güncelle → if d[v] > d[u]+w(u,v) then d[v]=d[u]+w(u,v)."},

 # --- L9 ---
 {"topic":"L9 · Bellman-Ford","q":"Bellman-Ford algoritmasının zaman karmaşıklığı nedir?",
  "options":["O(V²)","O(V·E)","O(E log V)","O(V + E)"],
  "correct":1,"explain":"Bellman-Ford V-1 tur döner, her turda E kenarı gevşetir → O(V·E)."},
 {"topic":"L9 · Bellman-Ford","q":"Bellman-Ford'un Dijkstra'ya göre temel avantajı nedir?",
  "options":["Daha hızlıdır","Negatif ağırlıklı kenarları işleyebilir ve negatif çevrim tespit eder","Daha az bellek kullanır","Sadece ağaçlarda çalışır"],
  "correct":1,"explain":"Bellman-Ford negatif kenarlarla çalışır ve negatif çevrim tespit eder; bedeli daha yüksek O(VE) zamanıdır."},

 # --- L10 ---
 {"topic":"L10 · MST","q":"V düğümlü bir grafın minimum spanning tree'sinde kaç kenar bulunur?",
  "options":["V","V−1","V+1","E−1"],
  "correct":1,"explain":"Bir spanning tree tüm V düğümü çevrimsiz bağlar; bir ağaçta tam olarak V−1 kenar vardır."},
 {"topic":"L10 · MST","q":"Kruskal algoritmasında çevrim (cycle) tespiti için hangi yapı kullanılır?",
  "options":["Priority queue","Union-Find (Disjoint Set)","Hash table","Stack"],
  "correct":1,"explain":"Kruskal, bir kenarın iki ucu aynı kümede mi diye Union-Find ile bakar; aynı kümedeyse kenar çevrim oluşturur ve atlanır."},
 {"topic":"L10 · MST","q":"Prim ve Kruskal algoritmaları hangi paradigmaya dayanır?",
  "options":["Dynamic programming","Greedy","Backtracking","Divide and conquer"],
  "correct":1,"explain":"Hem Prim hem Kruskal greedy'dir; her adımda yerel en iyi (en ucuz) kenarı seçerek MST kurarlar."},

 # --- L11 ---
 {"topic":"L11 · BFS/DFS","q":"BFS (Breadth-First Search) hangi veri yapısını kullanır?",
  "options":["Stack","Queue","Priority queue","Heap"],
  "correct":1,"explain":"BFS queue (FIFO) kullanır ve grafı seviye seviye gezer. DFS ise stack/recursion kullanır."},
 {"topic":"L11 · BFS/DFS","q":"BFS ve DFS'in zaman karmaşıklığı nedir?",
  "options":["O(V·E)","O(V²)","O(V + E)","O(E log V)"],
  "correct":2,"explain":"Her düğüm bir kez, her kenar bir kez işlenir → O(V+E). Her kenara yalnızca bir kez bakıldığı için O(V·E) değildir."},

 # --- L12 ---
 {"topic":"L12 · Knapsack","q":"Fractional Knapsack problemi optimal olarak hangi yöntemle çözülür?",
  "options":["Dynamic programming","Greedy (value/weight oranına göre)","Backtracking","BFS"],
  "correct":1,"explain":"Nesneler bölünebildiği için value/weight oranına göre azalan sırayla almak (greedy) optimaldir."},
 {"topic":"L12 · Knapsack","q":"0/1 Knapsack için aşağıdakilerden hangisi DOĞRUDUR?",
  "options":["Greedy her zaman optimal sonucu verir","Nesneler bölünebilir","Dynamic programming ile O(n·W) çözülür","Sadece negatif değerlerle çalışır"],
  "correct":2,"explain":"0/1'de nesne bölünemez ve greedy başarısız olabilir; DP ile O(n·W) zamanda optimal çözülür."},

 # --- L13 ---
 {"topic":"L13 · Topological Sort","q":"Kahn algoritması bir grafikte çevrim (cycle) olduğunu nasıl anlar?",
  "options":["Kenar sayısı V'den fazlaysa","Sonuç listesinin boyutu düğüm sayısına (V) eşit değilse","Tüm in-degree'ler 0 ise","Queue başta boşsa"],
  "correct":1,"explain":"Çevrimdeki düğümlerin in-degree'si hiç 0 olmaz, kuyruğa girmezler. Sonuçta result.size() != V ise çevrim vardır."},
]

print("MCQ loaded:", len(MCQ))
