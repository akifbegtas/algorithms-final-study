# -*- coding: utf-8 -*-
"""
Analysis of Algorithms - Final Exam Study Guide generator.
Builds a single self-contained interactive HTML file.
"""
import html as _html
import json
import re

import content_lectures
import content_mcq
import content_classic
import content_exams

# ----------------------------------------------------------------------------
# Mini markdown -> HTML renderer
# ----------------------------------------------------------------------------

def _esc(s):
    return _html.escape(s, quote=False)

def _inline(text):
    text = _esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+?)`", lambda m: "<code>%s</code>" % m.group(1), text)
    text = text.replace("->", "&rarr;").replace("=>", "&rArr;")
    return text

def md(text):
    if text is None:
        return ""
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)
    para = []

    def flush_para():
        if para:
            joined = " ".join(p.strip() for p in para if p.strip())
            if joined:
                out.append("<p>%s</p>" % _inline(joined))
            para.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_para()
            lang = stripped[3:].strip() or "text"
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            code = "\n".join(code_lines)
            out.append(render_code(code, lang))
            continue

        if stripped.startswith("### "):
            flush_para()
            out.append("<h4>%s</h4>" % _inline(stripped[4:]))
            i += 1
            continue
        if stripped.startswith("## "):
            flush_para()
            out.append("<h3>%s</h3>" % _inline(stripped[3:]))
            i += 1
            continue

        if stripped.startswith(":::"):
            flush_para()
            kind = "note"
            body = stripped[3:].strip()
            m = re.match(r"(note|tip|warn|exam)\s+(.*)", body)
            label = "Not"
            if m:
                kind = m.group(1)
                body = m.group(2)
                label = {"note": "Not", "tip": "İpucu", "warn": "Dikkat",
                         "exam": "Sınavda Çıkar"}.get(kind, "Not")
            buff = [body] if body else []
            i += 1
            while i < n and lines[i].strip() != ":::":
                buff.append(lines[i])
                i += 1
            i += 1
            inner = md("\n".join(buff))
            out.append('<div class="callout %s"><span class="callout-label">%s</span>%s</div>'
                       % (kind, label, inner))
            continue

        # table:  | a | b |   followed by a separator line  |---|---|
        if (stripped.startswith("|") and i + 1 < n
                and re.match(r'^\|?[\s:|-]+\|?$', lines[i + 1].strip())
                and '-' in lines[i + 1]):
            flush_para()
            header = [c.strip() for c in stripped.strip().strip('|').split('|')]
            i += 2  # skip header + separator
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            th = "".join("<th>%s</th>" % _inline(h) for h in header)
            tb = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _inline(c) for c in r)
                         for r in rows)
            out.append('<div class="tablewrap"><table><thead><tr>%s</tr></thead>'
                       '<tbody>%s</tbody></table></div>' % (th, tb))
            continue

        if stripped.startswith("- "):
            flush_para()
            raw = []
            while i < n:
                ls = lines[i].strip()
                if ls.startswith("- "):
                    raw.append(ls[2:])
                    i += 1
                elif raw and ls and not re.match(r'^(```|#{2,3}\s|:::|\||-\s|\d+\.\s)', ls):
                    raw[-1] += " " + ls   # wrapped continuation line
                    i += 1
                else:
                    break
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % _inline(it) for it in raw))
            continue

        if re.match(r"^\d+\.\s", stripped):
            flush_para()
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append("<li>%s</li>" % _inline(re.sub(r"^\d+\.\s", "", lines[i].strip())))
                i += 1
            out.append("<ol>%s</ol>" % "".join(items))
            continue

        if stripped == "":
            flush_para()
            i += 1
            continue

        para.append(line)
        i += 1

    flush_para()
    return "\n".join(out)


def render_code(code, lang="cpp"):
    code = code.strip("\n")
    escaped = _esc(code)
    lang_label = {"cpp": "C++", "python": "Python", "text": "Sözde Kod",
                  "pseudo": "Sözde Kod", "bash": "Terminal"}.get(lang, lang)
    cls = {"pseudo": "text"}.get(lang, lang)
    return ('<div class="codewrap"><div class="codebar"><span class="dot r"></span>'
            '<span class="dot y"></span><span class="dot g"></span>'
            '<span class="lang">%s</span>'
            '<button class="copybtn" onclick="copyCode(this)">Kopyala</button></div>'
            '<pre class="code"><code class="language-%s">%s</code></pre></div>'
            % (lang_label, cls, escaped))


def render_lecture(lec, idx):
    qa_html = []
    for j, (q, a) in enumerate(lec["qa"], 1):
        qa_html.append(
            '<details class="qa">'
            '<summary><span class="qnum">S%d</span>%s</summary>'
            '<div class="qa-body">%s</div></details>'
            % (j, _inline(q), md(a))
        )
    qa_block = "\n".join(qa_html)
    return f"""
<section id="{lec['code'].lower()}" class="lecture" data-section="lecture">
  <div class="lec-head">
    <span class="lec-chip">{lec['code']}</span>
    <div>
      <h2>{_inline(lec['title'])}</h2>
      <p class="lec-sub">{_inline(lec.get('subtitle',''))}</p>
    </div>
  </div>
  <div class="lec-body">
    {md(lec['body'])}
  </div>
  <div class="qa-wrap">
    <div class="qa-head">
      <h3>📝 {lec['code']} — 7 Çıkmış/Olası Soru <span class="muted">(tıkla, cevabı gör)</span></h3>
    </div>
    {qa_block}
  </div>
</section>
"""


def render_quiz(questions, qid, chip, chip_cls, title, subtitle, intro="", instant_feedback=False):
    data = json.dumps([{"correct": q["correct"]} for q in questions], ensure_ascii=False)
    cards = []
    for i, q in enumerate(questions):
        opts_list = q.get("options") or q.get("opts")
        exp = q.get("explain") or q.get("exp", "")
        topic = q.get("topic", "")
        topic_html = f'<span class="mcq-topic">{_inline(topic)}</span>' if topic else ''
        instant_attr = f' onchange="answerQuizQuestion(\'{qid}\',{i})"' if instant_feedback else ''
        feedback_html = f'<div class="question-feedback" id="{qid}_fb{i}"></div>' if instant_feedback else ''
        reveal_html = (
            f'<div class="reveal-row"><button type="button" class="btn reveal-answer" '
            f'id="{qid}_reveal{i}" onclick="revealQuizAnswer(\'{qid}\',{i})">Cevabı Göster</button></div>'
        ) if instant_feedback else ''
        opts = "".join(
            f'<label class="opt" data-o="{k}">'
            f'<input type="radio" name="{qid}_q{i}" value="{k}"{instant_attr}>'
            f'<span class="opt-key">{chr(65+k)}</span>'
            f'<span class="opt-txt">{_inline(o)}</span></label>'
            for k, o in enumerate(opts_list)
        )
        cards.append(
            f'<div class="mcq" id="{qid}_mcq{i}"><div class="mcq-q">'
            f'<span class="mcq-n">{i+1}</span>{topic_html}'
            f'<div class="mcq-text">{_inline(q["q"])}</div></div>'
            f'<div class="opts">{opts}</div>'
            f'{reveal_html}'
            f'{feedback_html}'
            f'<div class="explain" id="{qid}_exp{i}"><strong>Cevap &amp; Açıklama:</strong> {_inline(exp)}</div>'
            f'</div>'
        )
    cards_html = "\n".join(cards)
    intro_html = (f'<div class="callout note"><span class="callout-label">Bilgi</span>'
                  f'<p>{_inline(intro)}</p></div>') if intro else ''
    section_cls = "quiz-section instant-feedback" if instant_feedback else "quiz-section"
    return f"""
<section id="{qid}" class="{section_cls}" data-section="quiz">
  <div class="lec-head">
    <span class="lec-chip {chip_cls}">{chip}</span>
    <div><h2>{_inline(title)}</h2>
    <p class="lec-sub">{_inline(subtitle)}</p></div>
  </div>
  {intro_html}
  <div class="quiz-toolbar">
    <button class="btn primary" onclick="gradeQuiz('{qid}')">Bitir &amp; Puanla</button>
    <button class="btn ghost" onclick="resetQuiz('{qid}')">Sıfırla</button>
    <div class="score" id="{qid}_score"></div>
  </div>
  <div>{cards_html}</div>
  <div class="quiz-toolbar bottom">
    <button class="btn primary" onclick="gradeQuiz('{qid}')">Bitir &amp; Puanla</button>
    <div class="score" id="{qid}_score2"></div>
  </div>
</section>
<script>window.QUIZZES=window.QUIZZES||{{}};window.QUIZZES["{qid}"]={data};</script>
"""


def render_classic(items):
    blocks = []
    for i, it in enumerate(items, 1):
        blocks.append(
            f'<div class="classic" id="classic{i}">'
            f'<div class="classic-head"><span class="classic-n">K{i}</span>'
            f'<span class="classic-topic">{_inline(it.get("topic",""))}</span></div>'
            f'<div class="classic-prompt">{md(it["prompt"])}</div>'
            f'<details class="qa solution"><summary>✅ Çözümü / Cevap Anahtarını Göster</summary>'
            f'<div class="qa-body">{md(it["answer"])}</div></details>'
            f'</div>'
        )
    body = "\n".join(blocks)
    return f"""
<section id="klasik" class="classic-section" data-section="classic">
  <div class="lec-head">
    <span class="lec-chip alt2">KLASİK</span>
    <div><h2>Klasik Sorular — Kod Boşluk Doldurma</h2>
    <p class="lec-sub">Eksik kodu tamamla · çözümü altta gizli</p></div>
  </div>
  <div class="callout exam"><span class="callout-label">Sınavda Çıkar</span>
  <p>Bu bölümdeki sorular hocanın slaytlarındaki kod parçalarına dayanıyor. Boşlukları (<code>____</code>) zihninde doldur, sonra çözümü aç.</p></div>
  {body}
</section>
"""


CSS = r"""
:root{
  --bg:#0b1020; --bg2:#0f152b; --panel:#121a35; --panel2:#16203f;
  --ink:#e8edff; --muted:#9aa6c8; --line:#243057;
  --acc:#6ea8fe; --acc2:#8b7bff; --good:#37d399; --bad:#ff6b81; --warn:#ffcf6b;
  --chip:#1c2750; --code:#0c1124;
  --shadow:0 10px 30px rgba(0,0,0,.35);
}
[data-theme="light"]{
  --bg:#eef2fb; --bg2:#e7edfa; --panel:#ffffff; --panel2:#f5f8ff;
  --ink:#18213f; --muted:#5b6b94; --line:#d3ddf5;
  --chip:#e8eeff; --shadow:0 10px 30px rgba(40,60,120,.12);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(1200px 600px at 80% -10%,#1a2350 0%,transparent 60%),var(--bg);
  color:var(--ink);font-family:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif;
  line-height:1.65;-webkit-font-smoothing:antialiased}
[data-theme="light"] body{background:radial-gradient(1000px 500px at 85% -10%,#cdd8ff 0%,transparent 60%),var(--bg)}
a{color:var(--acc);text-decoration:none}
#progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--acc),var(--acc2));width:0;z-index:100;transition:width .1s}

/* layout */
.wrap{display:grid;grid-template-columns:280px 1fr;gap:0;max-width:1500px;margin:0 auto}
aside{position:sticky;top:0;height:100vh;overflow-y:auto;padding:22px 16px;border-right:1px solid var(--line);
  background:linear-gradient(180deg,var(--bg2),transparent)}
aside::-webkit-scrollbar{width:8px}aside::-webkit-scrollbar-thumb{background:var(--line);border-radius:8px}
.brand{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.brand .logo{width:38px;height:38px;border-radius:11px;background:linear-gradient(135deg,var(--acc),var(--acc2));
  display:grid;place-items:center;font-weight:800;color:#fff;box-shadow:var(--shadow)}
.brand h1{font-size:15px;margin:0;letter-spacing:.2px}
.brand small{color:var(--muted);font-size:11.5px}
.navsearch{width:100%;margin:14px 0 10px;padding:9px 12px;border-radius:10px;border:1px solid var(--line);
  background:var(--panel);color:var(--ink);font-size:13px;outline:none}
.navsearch:focus{border-color:var(--acc)}
nav a{display:flex;align-items:center;gap:9px;padding:8px 11px;border-radius:9px;color:var(--muted);
  font-size:13.5px;margin:2px 0;border:1px solid transparent;transition:.15s}
nav a:hover{background:var(--panel);color:var(--ink)}
nav a.active{background:var(--chip);color:var(--ink);border-color:var(--line)}
nav a .lc{font-size:11px;font-weight:700;color:var(--acc);min-width:30px}
nav .group{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin:14px 8px 4px;opacity:.7}
.theme-btn{margin-top:14px;width:100%;padding:9px;border-radius:10px;border:1px solid var(--line);
  background:var(--panel);color:var(--ink);cursor:pointer;font-size:13px}
.theme-btn:hover{border-color:var(--acc)}

main{padding:34px 40px 120px;min-width:0}
.hero{background:linear-gradient(135deg,var(--panel),var(--panel2));border:1px solid var(--line);
  border-radius:22px;padding:34px 34px 28px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-60px;top:-60px;width:240px;height:240px;
  background:radial-gradient(circle,rgba(110,168,254,.25),transparent 70%)}
.hero .kick{color:var(--acc);font-weight:700;letter-spacing:2px;font-size:12px;text-transform:uppercase}
.hero h2{font-size:30px;margin:8px 0 6px;line-height:1.2}
.hero p{color:var(--muted);margin:0;max-width:680px}
.stats{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
.stat{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:12px 16px;min-width:120px}
.stat b{display:block;font-size:22px}.stat span{color:var(--muted);font-size:12px}

section{margin-top:30px;background:linear-gradient(180deg,var(--panel),var(--panel2));
  border:1px solid var(--line);border-radius:20px;padding:26px 28px;box-shadow:var(--shadow);scroll-margin-top:18px}
.lec-head{display:flex;gap:16px;align-items:flex-start;margin-bottom:6px}
.lec-chip{flex:none;font-weight:800;font-size:13px;color:#fff;background:linear-gradient(135deg,var(--acc),var(--acc2));
  padding:7px 12px;border-radius:11px;box-shadow:var(--shadow)}
.lec-chip.alt{background:linear-gradient(135deg,#37d399,#1eb980)}
.lec-chip.alt2{background:linear-gradient(135deg,#ffcf6b,#ff9f43);color:#3a2a00}
.lec-chip.alt3{background:linear-gradient(135deg,#ff6b81,#d6336c)}
.lec-head h2{margin:0;font-size:22px}
.lec-sub{color:var(--muted);margin:3px 0 0;font-size:14px}
.lec-body{margin-top:14px}
.lec-body h3{font-size:18px;margin:22px 0 8px;color:var(--ink)}
.lec-body h4{font-size:15.5px;margin:16px 0 6px;color:var(--acc)}
.lec-body p{margin:9px 0}
.lec-body ul,.lec-body ol{margin:8px 0 8px 4px;padding-left:22px}
.lec-body li{margin:4px 0}
code{background:var(--chip);padding:2px 6px;border-radius:6px;font-family:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;
  font-size:.9em;color:#cfe0ff}
[data-theme="light"] code{color:#234}

/* code blocks */
.codewrap{margin:14px 0;border-radius:13px;overflow:hidden;border:1px solid var(--line);background:var(--code);box-shadow:var(--shadow)}
.codebar{display:flex;align-items:center;gap:7px;padding:9px 13px;background:#0a0f1f;border-bottom:1px solid var(--line)}
.dot{width:11px;height:11px;border-radius:50%}.dot.r{background:#ff5f57}.dot.y{background:#febc2e}.dot.g{background:#28c840}
.codebar .lang{margin-left:8px;font-size:11.5px;color:var(--muted);font-weight:600;letter-spacing:.5px}
.copybtn{margin-left:auto;background:var(--chip);border:1px solid var(--line);color:var(--ink);
  font-size:11.5px;padding:4px 10px;border-radius:7px;cursor:pointer}
.copybtn:hover{border-color:var(--acc);color:var(--acc)}
pre.code{margin:0;padding:15px 16px;overflow-x:auto;font-family:'JetBrains Mono',ui-monospace,Menlo,Consolas,monospace;
  font-size:13px;line-height:1.6;color:#dbe6ff}
pre.code code{background:transparent;padding:0;color:inherit}
pre.code .hljs{background:transparent;padding:0}
pre.code::-webkit-scrollbar{height:8px}pre.code::-webkit-scrollbar-thumb{background:var(--line);border-radius:8px}

/* callouts */
.callout{border-radius:13px;padding:13px 15px 13px 16px;margin:14px 0;border:1px solid var(--line);
  background:var(--bg);position:relative}
.callout p{margin:6px 0}
.callout-label{display:inline-block;font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.8px;
  padding:2px 9px;border-radius:30px;margin-bottom:4px}
.callout.note{border-left:4px solid var(--acc)} .callout.note .callout-label{background:rgba(110,168,254,.18);color:var(--acc)}
.callout.tip{border-left:4px solid var(--good)} .callout.tip .callout-label{background:rgba(55,211,153,.18);color:var(--good)}
.callout.warn{border-left:4px solid var(--bad)} .callout.warn .callout-label{background:rgba(255,107,129,.18);color:var(--bad)}
.callout.exam{border-left:4px solid var(--warn)} .callout.exam .callout-label{background:rgba(255,207,107,.2);color:var(--warn)}

/* tables */
.tablewrap{overflow-x:auto;margin:14px 0;border:1px solid var(--line);border-radius:12px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
thead th{background:var(--chip);color:var(--ink);text-align:left;padding:10px 13px;font-weight:700;
  border-bottom:2px solid var(--line);white-space:nowrap}
tbody td{padding:9px 13px;border-bottom:1px solid var(--line);color:#d4ddff;vertical-align:top}
[data-theme="light"] tbody td{color:#28335a}
tbody tr:last-child td{border-bottom:none}
tbody tr:nth-child(even){background:rgba(255,255,255,.02)}
table code{white-space:nowrap}

/* Q&A */
.qa-wrap{margin-top:22px;border-top:1px dashed var(--line);padding-top:16px}
.qa-head h3{font-size:16px;margin:0 0 12px}
.qa-head .muted{color:var(--muted);font-weight:400;font-size:13px}
details.qa{background:var(--bg);border:1px solid var(--line);border-radius:12px;margin:9px 0;overflow:hidden}
details.qa[open]{border-color:var(--acc)}
details.qa summary{cursor:pointer;padding:13px 16px;font-weight:600;font-size:14.5px;list-style:none;
  display:flex;gap:10px;align-items:flex-start;transition:.15s}
details.qa summary::-webkit-details-marker{display:none}
details.qa summary:hover{background:var(--panel)}
details.qa summary::after{content:"+";margin-left:auto;color:var(--acc);font-weight:800;font-size:18px;flex:none}
details.qa[open] summary::after{content:"–"}
.qnum{flex:none;font-size:11.5px;font-weight:800;color:#fff;background:var(--acc);padding:2px 8px;border-radius:20px;margin-top:1px}
.qa-body{padding:2px 18px 16px;color:var(--ink)}
.qa-body p{margin:8px 0;color:#d4ddff}
[data-theme="light"] .qa-body p{color:#28335a}
.solution summary{color:var(--good)} details.qa.solution[open]{border-color:var(--good)}
.solution summary::after{color:var(--good)}

/* quiz */
.quiz-toolbar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:16px 0}
.quiz-toolbar.bottom{margin-top:24px}
.btn{border:1px solid var(--line);background:var(--panel);color:var(--ink);padding:10px 18px;border-radius:11px;
  cursor:pointer;font-size:14px;font-weight:600}
.btn.primary{background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;border:none;box-shadow:var(--shadow)}
.btn.primary:hover{filter:brightness(1.07)}
.btn.ghost:hover{border-color:var(--acc)}
.score{font-weight:700;font-size:15px}
.mcq{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:12px 0}
.mcq-q{display:flex;gap:11px;align-items:flex-start;margin-bottom:11px}
.mcq-n{flex:none;width:27px;height:27px;border-radius:9px;background:var(--chip);color:var(--acc);font-weight:800;
  display:grid;place-items:center;font-size:13px}
.mcq-topic{flex:none;font-size:10.5px;font-weight:700;color:var(--muted);background:var(--panel);border:1px solid var(--line);
  padding:2px 8px;border-radius:20px;align-self:center}
.mcq-text{font-weight:600;font-size:14.5px}
.opts{display:grid;gap:8px}
.opt{display:flex;align-items:center;gap:11px;padding:10px 13px;border:1px solid var(--line);border-radius:11px;
  cursor:pointer;transition:.12s;background:var(--panel)}
.opt:hover{border-color:var(--acc)}
.opt input{accent-color:var(--acc);width:16px;height:16px;flex:none}
.opt-key{flex:none;width:22px;height:22px;border-radius:7px;background:var(--chip);display:grid;place-items:center;
  font-weight:700;font-size:12px;color:var(--muted)}
.opt-txt{font-size:14px}
.opt.correct{border-color:var(--good);background:rgba(55,211,153,.12)} .opt.correct .opt-key{background:var(--good);color:#042}
.opt.wrong{border-color:var(--bad);background:rgba(255,107,129,.12)} .opt.wrong .opt-key{background:var(--bad);color:#400}
.reveal-row{display:flex;justify-content:flex-end;margin-top:10px}
.btn.reveal-answer{padding:7px 12px;border-radius:9px;font-size:12.5px;color:var(--acc);background:var(--bg)}
.btn.reveal-answer:hover{border-color:var(--acc);background:var(--chip)}
.question-feedback{display:none;margin-top:11px;padding:10px 13px;border-radius:10px;font-size:13.5px;
  font-weight:700;border:1px solid var(--line);background:var(--panel)}
.question-feedback.show{display:block}
.question-feedback.good{border-color:var(--good);color:var(--good);background:rgba(55,211,153,.1)}
.question-feedback.bad{border-color:var(--bad);color:var(--bad);background:rgba(255,107,129,.1)}
.question-feedback.warn{border-color:var(--warn);color:var(--warn);background:rgba(255,207,107,.1)}
.explain{display:none;margin-top:11px;padding:11px 13px;border-radius:10px;background:var(--panel2);
  border:1px solid var(--line);font-size:13.5px;color:var(--muted)}
.explain.show{display:block}
.explain strong{color:var(--ink)}
.result-banner{margin:6px 0 0;padding:16px 18px;border-radius:14px;font-weight:700;display:none}
.result-banner.show{display:block}

/* classic */
.classic{background:var(--bg);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:14px 0}
.classic-head{display:flex;gap:10px;align-items:center;margin-bottom:8px}
.classic-n{flex:none;font-weight:800;font-size:12px;color:#3a2a00;background:linear-gradient(135deg,#ffcf6b,#ff9f43);
  padding:3px 10px;border-radius:20px}
.classic-topic{font-size:12px;color:var(--muted);font-weight:600}

footer{max-width:1500px;margin:0 auto;padding:24px 40px 50px;color:var(--muted);font-size:12.5px;text-align:center}
.toTop{position:fixed;right:22px;bottom:22px;width:46px;height:46px;border-radius:50%;border:1px solid var(--line);
  background:var(--panel);color:var(--ink);cursor:pointer;display:none;place-items:center;box-shadow:var(--shadow);font-size:18px;z-index:50}
.toTop.show{display:grid}
.hidden{display:none !important}

.mobtop{display:none}
@media(max-width:980px){
  .wrap{grid-template-columns:1fr}
  aside{display:none}
  main{padding:18px 16px 90px}
  .mobtop{display:flex;position:sticky;top:0;z-index:40;align-items:center;gap:10px;padding:11px 14px;
    background:var(--bg2);border-bottom:1px solid var(--line);margin:-18px -16px 14px}
  .mobtop select{flex:1;padding:9px;border-radius:10px;background:var(--panel);color:var(--ink);border:1px solid var(--line)}
  .hero h2{font-size:23px}
}
@media print{aside,.toTop,.quiz-toolbar,.theme-btn,.mobtop{display:none!important}
  details.qa,.explain{display:block!important} .explain{display:block!important}
  body{background:#fff;color:#000} section{break-inside:avoid;box-shadow:none}}
"""

JS = r"""
function copyCode(btn){
  try{
    var code = btn.closest('.codewrap').querySelector('code').innerText;
    navigator.clipboard.writeText(code).then(function(){
      var o=btn.textContent; btn.textContent='Kopyalandı ✓';
      setTimeout(function(){btn.textContent=o;},1200);
    });
  }catch(e){}
}
function getQuizData(id){
  return (window.QUIZZES&&window.QUIZZES[id])||[];
}
function correctAnswerText(id,i,ci){
  return String.fromCharCode(65+ci);
}
function setQuestionFeedback(id,i,kind,text){
  var fb=document.getElementById(id+'_fb'+i);
  if(!fb) return;
  fb.className='question-feedback show '+kind;
  fb.textContent=text;
}
function markQuizQuestion(id,i,revealUnanswered){
  var data=getQuizData(id);
  if(!data[i]) return {answered:false,correct:false};
  var picked=document.querySelector('input[name="'+id+'_q'+i+'"]:checked');
  var opts=document.querySelectorAll('#'+id+'_mcq'+i+' .opt');
  opts.forEach(function(o){o.classList.remove('correct','wrong');});
  var ci=data[i].correct;
  opts.forEach(function(o){
    if(parseInt(o.getAttribute('data-o'))===ci) o.classList.add('correct');
  });
  var ex=document.getElementById(id+'_exp'+i);
  if(picked){
    var pi=parseInt(picked.value);
    var ok=pi===ci;
    if(!ok){
      var w=document.querySelector('#'+id+'_mcq'+i+' .opt[data-o="'+pi+'"]');
      if(w) w.classList.add('wrong');
    }
    setQuestionFeedback(id,i,ok?'good':'bad',
      ok ? 'Doğru. Cevap: '+correctAnswerText(id,i,ci)
         : 'Yanlış. Doğru cevap: '+correctAnswerText(id,i,ci));
    if(ex) ex.classList.add('show');
    return {answered:true,correct:ok};
  }
  if(revealUnanswered){
    setQuestionFeedback(id,i,'warn','Cevaplanmadı. Doğru cevap: '+correctAnswerText(id,i,ci));
    if(ex) ex.classList.add('show');
  }
  return {answered:false,correct:false};
}
function revealQuizAnswer(id,i){
  var data=getQuizData(id);
  if(!data[i]) return;
  var ci=data[i].correct;
  document.querySelectorAll('#'+id+'_mcq'+i+' .opt').forEach(function(o){
    o.classList.remove('correct','wrong');
    if(parseInt(o.getAttribute('data-o'))===ci) o.classList.add('correct');
  });
  setQuestionFeedback(id,i,'warn','Doğru cevap: '+correctAnswerText(id,i,ci));
  var ex=document.getElementById(id+'_exp'+i); if(ex) ex.classList.add('show');
  var btn=document.getElementById(id+'_reveal'+i); if(btn) btn.textContent='Cevap Gösterildi';
}
function setQuizScore(id,correct,answered,total,prefix){
  var pct=total?Math.round(correct/total*100):0;
  var msg=(prefix||'Skor')+': '+correct+' / '+total+'  ('+pct+'%)  ·  '+answered+' işaretlendi';
  ['','2'].forEach(function(sx){
    var el=document.getElementById(id+'_score'+sx);
    if(el){el.textContent=msg; el.style.color=pct>=70?'var(--good)':(pct>=50?'var(--warn)':'var(--bad)');}
  });
}
function updateInstantScore(id){
  var sec=document.getElementById(id);
  if(!sec||!sec.classList.contains('instant-feedback')) return;
  var data=getQuizData(id), correct=0, answered=0;
  for(var i=0;i<data.length;i++){
    var picked=document.querySelector('input[name="'+id+'_q'+i+'"]:checked');
    if(picked){
      answered++;
      if(parseInt(picked.value)===data[i].correct) correct++;
    }
  }
  setQuizScore(id,correct,answered,data.length,'Anlık');
}
function answerQuizQuestion(id,i){
  markQuizQuestion(id,i,false);
  updateInstantScore(id);
}
function gradeQuiz(id){
  var data=getQuizData(id); var correct=0, answered=0;
  for(var i=0;i<data.length;i++){
    var result=markQuizQuestion(id,i,true);
    if(result.answered) answered++;
    if(result.correct) correct++;
  }
  setQuizScore(id,correct,answered,data.length,'Skor');
  var first=document.getElementById(id+'_mcq0'); if(first)first.scrollIntoView({behavior:'smooth',block:'start'});
}
function resetQuiz(id){
  var data=getQuizData(id);
  for(var i=0;i<data.length;i++){
    document.querySelectorAll('input[name="'+id+'_q'+i+'"]').forEach(function(r){r.checked=false;});
    document.querySelectorAll('#'+id+'_mcq'+i+' .opt').forEach(function(o){o.classList.remove('correct','wrong');});
    var fb=document.getElementById(id+'_fb'+i);
    if(fb){fb.className='question-feedback'; fb.textContent='';}
    var btn=document.getElementById(id+'_reveal'+i); if(btn) btn.textContent='Cevabı Göster';
    var ex=document.getElementById(id+'_exp'+i); if(ex)ex.classList.remove('show');
  }
  ['','2'].forEach(function(sx){var el=document.getElementById(id+'_score'+sx); if(el)el.textContent='';});
  var sec=document.getElementById(id); if(sec)sec.scrollIntoView({behavior:'smooth',block:'start'});
}
// search filter
function runSearch(q){
  q=(q||'').toLowerCase().trim();
  document.querySelectorAll('details.qa').forEach(function(d){
    var t=d.textContent.toLowerCase();
    d.classList.toggle('hidden', q && t.indexOf(q)<0);
  });
  document.querySelectorAll('.mcq,.classic').forEach(function(d){
    var t=d.textContent.toLowerCase();
    d.classList.toggle('hidden', q && t.indexOf(q)<0);
  });
}
// theme
function toggleTheme(){
  var cur=document.documentElement.getAttribute('data-theme')==='light'?'':'light';
  document.documentElement.setAttribute('data-theme',cur);
  try{localStorage.setItem('aa_theme',cur);}catch(e){}
  document.querySelectorAll('.theme-btn').forEach(function(b){b.textContent=cur==='light'?'🌙 Koyu Tema':'☀️ Açık Tema';});
}
// nav + progress + scrollspy
document.addEventListener('DOMContentLoaded',function(){
  try{var t=localStorage.getItem('aa_theme'); if(t){document.documentElement.setAttribute('data-theme',t);
    document.querySelectorAll('.theme-btn').forEach(function(b){b.textContent='🌙 Koyu Tema';});}}catch(e){}
  if(window.hljs){try{hljs.highlightAll();}catch(e){}}
  var secs=[].slice.call(document.querySelectorAll('section[id]'));
  var links=[].slice.call(document.querySelectorAll('nav a'));
  var toTop=document.querySelector('.toTop');
  function onScroll(){
    var sc=document.documentElement.scrollTop||document.body.scrollTop;
    var h=document.documentElement.scrollHeight-document.documentElement.clientHeight;
    var p=document.getElementById('progress'); if(p)p.style.width=(sc/h*100)+'%';
    if(toTop)toTop.classList.toggle('show',sc>500);
    var cur=secs[0]?secs[0].id:null;
    secs.forEach(function(s){ if(s.getBoundingClientRect().top<140) cur=s.id; });
    links.forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+cur);});
  }
  document.addEventListener('scroll',onScroll,{passive:true}); onScroll();
});
function goTop(){window.scrollTo({top:0,behavior:'smooth'});}
function mobJump(sel){ if(sel){location.hash=sel;} }
"""


def build():
    lectures = content_lectures.LECTURES
    mcq = content_mcq.MCQ
    classic = content_classic.CLASSIC
    exams = sorted(content_exams.EXAMS, key=lambda e: e["year"])  # 2023-24, 2024-25

    total_qa = sum(len(l["qa"]) for l in lectures)
    total_exam_q = sum(len(e["questions"]) for e in exams)

    # nav
    nav_links = ['<div class="group">Dersler</div>']
    for l in lectures:
        nav_links.append(
            f'<a href="#{l["code"].lower()}"><span class="lc">{l["code"]}</span>'
            f'<span>{_inline(l["title"].split("—")[0].strip())}</span></a>'
        )
    nav_links.append('<div class="group">Sınav Hazırlık</div>')
    nav_links.append(f'<a href="#test"><span class="lc">✔</span><span>Çoktan Seçmeli Test ({len(mcq)})</span></a>')
    nav_links.append('<a href="#klasik"><span class="lc">✎</span><span>Klasik Sorular (Kod)</span></a>')
    nav_links.append('<div class="group">Çıkmış Sınavlar</div>')
    for e in exams:
        nav_links.append(f'<a href="#{e["id"]}"><span class="lc">★</span>'
                         f'<span>Final {e["year"]} ({len(e["questions"])})</span></a>')
    nav_html = "\n".join(nav_links)

    # mobile select
    mob_opts = ['<option value="">Bölüme atla…</option>']
    for l in lectures:
        mob_opts.append(f'<option value="#{l["code"].lower()}">{l["code"]} — {_inline(l["title"].split("—")[0].strip())}</option>')
    mob_opts.append('<option value="#test">Çoktan Seçmeli Test</option>')
    mob_opts.append('<option value="#klasik">Klasik Sorular</option>')
    for e in exams:
        mob_opts.append(f'<option value="#{e["id"]}">Çıkmış Final {e["year"]}</option>')
    mob_html = "".join(mob_opts)

    # sections
    body_sections = []
    for i, l in enumerate(lectures):
        body_sections.append(render_lecture(l, i))
    body_sections.append(render_quiz(mcq, "test", "TEST", "alt", "Çoktan Seçmeli Sınav",
                                     f"{len(mcq)} soru · tüm konular · otomatik puanlama"))
    body_sections.append(render_classic(classic))
    for e in exams:
        body_sections.append(render_quiz(e["questions"], e["id"], "ÇIKMIŞ", "alt3",
                                         f"Çıkmış Final · {e['year']}", e["meta"], e["intro"],
                                         instant_feedback=True))
    sections_html = "\n".join(body_sections)

    head = (
        '<!DOCTYPE html><html lang="tr" data-theme=""><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Analysis of Algorithms — Final Çalışma Kılavuzu</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">'
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">'
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>'
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/cpp.min.js"></script>'
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>'
        "<style>" + CSS + "</style></head><body>"
        '<div id="progress"></div>'
    )

    hero = f"""
<main>
  <div class="mobtop">
    <span class="lec-chip" style="font-size:11px">AoA</span>
    <select onchange="mobJump(this.value)">{mob_html}</select>
    <button class="btn ghost" style="padding:8px 10px" onclick="toggleTheme()">☀︎</button>
  </div>
  <div class="hero">
    <div class="kick">Final Sınavı · Çalışma Kılavuzu</div>
    <h2>Analysis of Algorithms — Tam Tekrar Seti</h2>
    <p>13 dersin konu anlatımı (kod parçalarıyla), her ders için 7 detaylı soru-cevap,
    {len(mcq)} soruluk otomatik puanlı çoktan seçmeli sınav, kod-boşluk-doldurmaca klasik sorular
    ve <strong>iki çıkmış final sınavı</strong> (2023-24 &amp; 2024-25) çözümleriyle. Başarılar! 🎯</p>
    <div class="stats">
      <div class="stat"><b>13</b><span>Ders / Konu</span></div>
      <div class="stat"><b>{total_qa}</b><span>Detaylı Soru-Cevap</span></div>
      <div class="stat"><b>{len(mcq)}</b><span>Çoktan Seçmeli</span></div>
      <div class="stat"><b>{len(classic)}</b><span>Klasik Kod Sorusu</span></div>
      <div class="stat"><b>{total_exam_q}</b><span>Çıkmış Soru · 2 final</span></div>
    </div>
  </div>
"""

    aside = (
        '<aside><div class="brand"><div class="logo">AA</div>'
        '<div><h1>Analysis of Algorithms</h1><small>Final • Çalışma Kılavuzu</small></div></div>'
        '<input class="navsearch" placeholder="🔍 Soru/konu ara…" oninput="runSearch(this.value)">'
        '<nav>' + nav_html + '</nav>'
        '<button class="theme-btn" onclick="toggleTheme()">☀️ Açık Tema</button>'
        '</aside>'
    )

    foot = (
        '</main></div>'  # close <main> and the .wrap grid
        '<button class="toTop" onclick="goTop()">↑</button>'
        '<footer>Bu kılavuz, yüklenen L1–L13 ders slaytlarından üretilmiştir. '
        'Kod örnekleri standart C++/sözde kod olarak yeniden yazılmıştır — sınavda hocanın '
        'gösterimi farklıysa onu esas al. · Hazırlık: kişisel çalışma amaçlı.</footer>'
        '<script>' + JS + '</script></body></html>'
    )

    html = head + '<div class="wrap">' + aside + hero + sections_html + foot
    return html


if __name__ == "__main__":
    out = build()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("WROTE index.html  bytes=", len(out))
