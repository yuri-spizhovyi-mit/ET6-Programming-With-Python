# Create an .ics calendar file for the 5-day/week Measurement study plan
from datetime import datetime
from uuid import uuid4

ics_lines = []
ics_lines.append("BEGIN:VCALENDAR")
ics_lines.append("VERSION:2.0")
ics_lines.append("PRODID:-//Yuri Study Plans//Measurement Mon-Fri//EN")
ics_lines.append("CALSCALE:GREGORIAN")
ics_lines.append("METHOD:PUBLISH")

tz = "America/Vancouver"
default_time = {"hour": 9, "minute": 0, "duration_minutes": 90}  # 9:00–10:30 AM local


def dtstr(y, m, d, h=18, mi=0):
    return f"DTSTART;TZID={tz}:{y:04d}{m:02d}{d:02d}T{h:02d}{mi:02d}00\nDTEND;TZID={tz}:{y:04d}{m:02d}{d:02d}T{(h + (mi + 60) // 60) % 24:02d}{(mi + 60) % 60:02d}00"


nowstamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")


def add_event(y, m, d, summary, description):
    uid = str(uuid4()) + "@yuri-study-plan"
    ics_lines.append("BEGIN:VEVENT")
    ics_lines.append(f"UID:{uid}")
    ics_lines.append(f"DTSTAMP:{nowstamp}")
    ics_lines.append(dtstr(y, m, d))
    ics_lines.append(f"SUMMARY:{summary}")
    # Escape commas and semicolons per RFC
    desc = (
        description.replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace(",", "\\,")
        .replace(";", "\\;")
    )
    ics_lines.append(f"DESCRIPTION:{desc}")
    ics_lines.append("END:VEVENT")


# Week 1 – Chapter 1.1 & 1.2
add_event(
    2025,
    8,
    11,
    "Measurement Study — Chapter 1.1 Lesson 1",
    "Read p.4–6 (1.1 Imperial Measures of Length).\\nComplete Examples 1–4.\\nDo Section A: Ex. 3–7.",
)
add_event(
    2025,
    8,
    12,
    "Measurement Study — Chapter 1.1 Lesson 2",
    "Review p.4–6.\\nDo Section B: Ex. 8–18 (choose any 5).",
)
add_event(
    2025,
    8,
    13,
    "Measurement Study — Chapter 1.1 Lesson 3",
    "Review p.4–6.\\nDo Section C: Ex. 19–22 (all).",
)
add_event(
    2025,
    8,
    14,
    "Measurement Study — Chapter 1.2 Lesson 1",
    "Read p.13–15 (Math Lab).\\nDo activities A–C.\\nStart Assess Your Understanding Q1–3.",
)
add_event(
    2025,
    8,
    15,
    "Measurement Study — Chapter 1.2 Lesson 2",
    "Review p.13–15.\\nComplete Assess Your Understanding Q4–6.",
)

# Week 2 – finish 1.2; Chapter 1.3
add_event(
    2025,
    8,
    18,
    "Measurement Study — Chapter 1.2 Lesson 3",
    "Review the full chapter.\\nFinish any pending measurements/notes from Math Lab.",
)
add_event(
    2025,
    8,
    19,
    "Measurement Study — Chapter 1.3 Lesson 1",
    "Read p.16–18 (Relating SI and Imperial Units).\\nExamples 1–2 and Check Your Understanding Q1–2.\\nStart Section A: Ex. 4–5.",
)
add_event(
    2025,
    8,
    20,
    "Measurement Study — Chapter 1.3 Lesson 2",
    "Review p.16–18.\\nExamples 3–4 and Check Your Understanding Q3–4.\\nSection B: Ex. 6–8.",
)
add_event(
    2025,
    8,
    21,
    "Measurement Study — Chapter 1.3 Lesson 3",
    "Review key conversions.\\nSection B: Ex. 9–13 (all).",
)
add_event(
    2025,
    8,
    22,
    "Measurement Study — Chapter 1.4 Lesson 1",
    "Read p.26–30 (SA of Right Pyramids & Cones).\\nExamples 1–2 and Check Your Understanding Q1–2.\\nSection A: Ex. 4–5.",
)

# Week 3 – Chapter 1.4 & 1.5
add_event(
    2025,
    8,
    25,
    "Measurement Study — Chapter 1.4 Lesson 2",
    "Review p.26–33.\\nExamples 3–4 and Check Your Understanding Q3–4.\\nSection A: Ex. 6–8.",
)
add_event(
    2025,
    8,
    26,
    "Measurement Study — Chapter 1.4 Lesson 3",
    "Review formulas (lateral area & SA).\\nSection B–C: Ex. 9–21 (all).",
)
add_event(
    2025,
    8,
    27,
    "Measurement Study — Chapter 1.5 Lesson 1",
    "Read p.36–39 (Volumes of Right Pyramids & Cones).\\nExamples 1–2 and Check Your Understanding Q1–2.\\nSection A: Ex. 4–5.",
)
add_event(
    2025,
    8,
    28,
    "Measurement Study — Chapter 1.5 Lesson 2",
    "Review p.36–41.\\nExamples 3–4 and Check Your Understanding Q3–4.\\nSection A: Ex. 6–7.",
)
add_event(
    2025,
    8,
    29,
    "Measurement Study — Chapter 1.5 Lesson 3",
    "Review volume relationships (1/3 of prism/cylinder).\\nSection B–C: Ex. 8–22 (all).",
)

# Week 4 – Chapter 1.6 & start 1.7
add_event(
    2025,
    9,
    1,
    "Measurement Study — Chapter 1.6 Lesson 1",
    "Read p.45–47 (Sphere — Surface Area).\\nExamples 1–2 and Check Your Understanding Q1–2.\\nSection A: Ex. 3–4.",
)
add_event(
    2025,
    9,
    2,
    "Measurement Study — Chapter 1.6 Lesson 2",
    "Read p.48–50 (Sphere — Volume; Hemispheres).\\nExamples 3–4 and Check Your Understanding Q3–4.\\nSection A: Ex. 5–7.",
)
add_event(
    2025,
    9,
    3,
    "Measurement Study — Chapter 1.6 Lesson 3",
    "Full review of sphere formulas.\\nSection B–C: Ex. 8–24 (all).",
)
add_event(
    2025,
    9,
    4,
    "Measurement Study — Chapter 1.7 Lesson 1",
    "Read p.55–57 (Composite Objects).\\nExamples 1–2 and Check Your Understanding Q1–2.\\nSection A: Ex. 3–4.",
)
add_event(
    2025,
    9,
    5,
    "Measurement Study — Chapter 1.7 Lesson 2",
    "Read p.58 (Example 3).\\nSection A: Ex. 5–6.",
)

# Week 5 – finish 1.7
add_event(
    2025,
    9,
    8,
    "Measurement Study — Chapter 1.7 Lesson 3",
    "Review the full chapter.\\nSection B–C: Ex. 7–13 (all).",
)

ics_lines.append("END:VCALENDAR")

path = "measurement-study-plan-mon-fri.ics"
with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(ics_lines))
