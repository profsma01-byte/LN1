#!/usr/bin/env python3
"""Full rebuild of all 32 lecture TXT files with varied, non-repetitive narration."""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
_ROOT = _os.path.dirname(_HERE)
if _os.getcwd() != _ROOT and not _os.path.isdir("PhD_Marriage_and_Family_Therapy_Lectures"):
    _os.chdir(_ROOT)
import os

from generate_lectures import COURSES, EXAMPLES, DIALOGUE_TEMPLATES
from narration_variants2 import TECHNIQUE_STYLES, build_extra_labs
from narration_variants3 import SCENARIO_TEMPLATES, LAB_CLOSERS, EXAMPLES_TAIL, CITIES
import narration_variants4 as V4
from glossary import GLOSSARY
from practical_frames import PRACTICAL_STYLES_2, choose_frame

COURSE_TERM_OVERRIDES = {
    ("MFLT.960", "Defence"): "the oral examination in which the doctoral candidate presents and defends the dissertation before a committee.",
    ("MFLT.928", "Health"): "physical and emotional wellbeing; in this course, sexual health includes knowledge, safety, consent, and access to good care.",
    ("MFLT.930", "Career"): "the long-term development of one's professional life, including specialisation, reputation, and sustainability.",
}
from narration_variants import (
    BRIDGE_A, MISTAKES_B, THERAPIST_C, CHECK_D, STEP_E,
    PRACTICAL_STYLES, CASE_STYLES, SUMMARY_CLOSERS, TRUTHS,
)

BASE = "PhD_Marriage_and_Family_Therapy_Lectures"


CONNECTORS = [
"When therapists skip these steps, families feel rushed, and rushing breeds resistance. When therapists follow them, even imperfectly, families relax, because structure communicates care. I have seen a single well-run first session change the direction of an entire family's year.",
"What you have just rehearsed is the ordinary backbone of extraordinary work. No client will ever thank you for a clever theory, but many will thank you for the day you sat still, listened, and then offered one clear next step.",
"Notice that every step is designed to protect someone: the child, the quiet parent, the therapist, the absent relative. Family therapy is a protective craft before it is a clever one.",
"In practice, these steps will not always run in order. A crisis may interrupt step three; a disclosure may reopen step one. That is normal. The frame is a map, not a prison.",
"These steps take courage as much as skill. It takes courage to ask about violence, to name a secret, to sit with tears, and to say 'I do not know, but I will find out'. Courage can be practised, and this lab is that practice.",
"What families remember is not the model you used. They remember whether you were honest, whether you were fair, and whether you gave them something real to do when they got home. Every step here serves those three memories.",
]

PROTECTED = {"Bowen", "Minuchin", "Satir", "Gottman", "Erikson", "Piaget",
             "Narrative", "Solution-Focused", "Family", "Therapy"}


def soft_lower(title):
    """Lowercase a concept title for mid-sentence use, preserving proper nouns and acronyms."""
    keep = {"Bowen", "Minuchin", "Satir", "Gottman", "Erikson", "Piaget",
            "PTSD", "ACEs", "ADHD", "EFT", "Gottman"}
    words = []
    for w in title.split():
        if w in keep or (w.isupper() and len(w) > 1):
            words.append(w)
        else:
            words.append(w[0].lower() + w[1:] if w else w)
    return " ".join(words)




def concept_module(i, title, core, course_title):
    course_index = sum(ord(c) for c in course_title) % 97
    city = CITIES[(i * 3 + course_index) % len(CITIES)]
    tl = soft_lower(title)
    ex = SCENARIO_TEMPLATES[(i * 5 + course_index) % len(SCENARIO_TEMPLATES)].format(city=city, tl=tl)
    tail = EXAMPLES_TAIL[(i * 3 + course_index) % len(EXAMPLES_TAIL)]
    dlg = V4.DIALOGUES_13[i % len(V4.DIALOGUES_13)]
    bridge = V4.BRIDGE_A[i % len(V4.BRIDGE_A)].format(t=title)
    mistakes = MISTAKES_B[(i * 3) % len(MISTAKES_B)]
    therapist = THERAPIST_C[(i * 7) % len(THERAPIST_C)]
    check = CHECK_D[(i * 11) % len(CHECK_D)]
    step = STEP_E[(i * 5) % len(STEP_E)]

    return f"""
MODULE {i+1}: {title}
----------------------------------------------------------------

My dear students, let us now turn our attention to {title}. This is a very important topic in {course_title}. Please listen carefully, because what you learn here will help you in the clinic, in the church, in the mosque, and in your own home.

{core}

{bridge}

Now, let us look at this in real life. {ex}

You see, my students, this example shows {tl} in action. The problem was not only in one person. The problem lived in the pattern of interaction between them. When the pattern changed, the whole family changed. {tail}

Let me give you a short dialogue to show how a therapist can handle this topic in a session:

{dlg}

{therapist}

{mistakes}

{check}

{step}

Quick reflection: Write in your notebook three ways {title} applies to families in your community. Bring your answer to class next week. We will discuss together.

"""


def practical_module(i, title, scenario, course_title):
    frame_key = choose_frame(title + " " + scenario)
    if frame_key:
        style_name, steps = PRACTICAL_STYLES_2[frame_key]
    else:
        style_name, steps = PRACTICAL_STYLES[i % len(PRACTICAL_STYLES)]
    ex = CONNECTORS[(i * 3 + len(course_title)) % len(CONNECTORS)]
    step_text = "\n\n".join(steps)
    return f"""
REAL LIFE PRACTICAL {i+1}: {title}
----------------------------------------------------------------

My dear students, theory without practice is empty. So let us do a real life practical on {title}. We will work through it in the style of {style_name}, which is one of the practical frames you will use in different settings.

Scenario: {scenario}

Let me walk you through this practical step by step, as you would do it in real life.

{step_text}

{ex}

You see, this practical is not difficult. It needs patience, respect, and skill. If you follow these steps, you will help many families. Practice this practical with a classmate this week. One person will be the therapist, the others will be the family. Switch roles after twenty minutes. Write down what you learned.

Important note: Always respect culture and faith. In Nigeria and in many African homes, elders are respected, faith is important, and the family is extended. Do not fight culture. Work with culture. Use proverbs, prayers, and respectful language where appropriate. The family will accept help faster when they feel their values are honoured.

"""


def case_module(i, title, story, course_title):
    steps = CASE_STYLES[i % len(CASE_STYLES)]
    return f"""
CASE STUDY {i+1}: {title}
----------------------------------------------------------------

My dear students, let us learn from a real case. I will tell you the story, and you will think like a therapist.

{story}

Now let us analyse this case together, using six questions.

{steps[0]} The family names one problem, but the real problem is often deeper. A family may say "our son is stubborn", while the true issue is marital conflict, neglect, or trauma. Look deeper with care, and never argue with the family's account; simply add to it.

{steps[1]} Who is in the family? Who holds power? Who is close, and who is distant? Where is the triangle? Map the system in your mind, and then check the map with the family.

{steps[2]} Maybe the family prays together. Maybe the parents work hard. Maybe the children are talented. Build on strengths. Do not only look at problems.

{steps[3]} Choose one clear intervention from {course_title}. Do not try everything at once. Explain it simply, demonstrate it, and practise it in the room.

{steps[4]} Is there abuse? Is there danger? Is a referral needed? Protect life first. If there is violence, make a safety plan. If there is mental illness, refer. Ethics is protection, not paperwork.

{steps[5]} Tell the family exactly what you will do, what you hope they will do, and what you will celebrate if it works. Give hope, and end with encouragement.

Let me ask you: if you were the therapist in this case, what would you do first? Write your answer in your notebook. Discuss with your group. There is no single perfect answer, but there are better and worse answers. Choose the answer that is respectful, safe, and practical.

{V4.CASE_CLOSERS[i % len(V4.CASE_CLOSERS)]}

"""


def build(course):
    (code, title, folder, overview, objectives, concepts,
     practicals, cases, techniques, terms) = course
    p = []
    p.append(f"""
================================================================================
TRIUNE BIBLICAL UNIVERSITY GLOBAL EXTENSION, USA
PHD IN MARRIAGE AND FAMILY LIFE THERAPY
================================================================================
COURSE CODE: {code}
COURSE TITLE: {title}
CREDIT HOURS: 3 CH
LECTURE NARRATION: SPOKEN LECTURE IN SIMPLE ENGLISH
WITH REAL LIFE PRACTICALS
================================================================================

WELCOME, MY DEAR STUDENTS
----------------------------------------------------------------

Good morning, my dear students. Good afternoon, depending on when you are listening to this lecture. Welcome to {code} - {title}. I am happy to be with you in this spoken lecture. Please find a quiet place, bring your notebook and pen, and listen with an open heart and a sharp mind.

This course is part of your PhD in Marriage and Family Therapy at Triune Biblical University Global Extension, USA. You are preparing to become an expert therapist who can help couples, families, children, and communities. This is a noble calling. Families are the foundation of society and of the church. When families are strong, communities are strong. When families are broken, society feels the pain.

In this lecture, I will speak in simple English. I will use real life examples from Nigeria, Africa, and the world. I will tell you stories of families in Ibadan, Lagos, Enugu, Kano, Abuja, and other places. These stories will help you understand theory in a practical way. Please listen, write notes, and think about how you will apply each lesson in your own ministry and practice.

How to use this lecture:
1. Listen to the full lecture once, without stopping.
2. Listen again and write key points in your notebook.
3. Do the practicals and case studies with a partner or group.
4. Answer the self-test questions at the end.
5. Do the assignment and bring it to class or submit online.

Learning Objectives - By the end of this course, you will be able to:
""")
    for i, o in enumerate(objectives, 1):
        p.append(f"{i}. {o}\n")

    p.append(f"""
Overview of the Course
----------------------------------------------------------------

{overview}

In this course, we will move from theory to practice. We will learn key concepts, we will see real life examples, we will do practical exercises, we will study cases, and we will learn techniques you can use immediately. At the end, you will have a strong foundation for advanced work in {title}.

Let us begin. Open your mind. Be ready to learn. Be ready to change. Be ready to help others.


PART ONE: CORE CONCEPTS - SPOKEN LECTURE
================================================================
""")
    for i, (ct, core) in enumerate(concepts):
        p.append(concept_module(i, ct, core, title))

    p.append("""
PART TWO: REAL LIFE PRACTICALS - STEP BY STEP
================================================================
""")
    for i, item in enumerate(practicals):
        p.append(practical_module(i, item[0], " ".join(item[1:]), title))
    p.append(build_extra_labs(title, concepts))

    p.append("""
PART THREE: CASE STUDIES - THINK LIKE A THERAPIST
================================================================
""")
    for i, (ct, cs) in enumerate(cases):
        p.append(case_module(i, ct, cs, title))

    p.append(f"""
PART FOUR: KEY TECHNIQUES YOU MUST MASTER
----------------------------------------------------------------

My dear students, in {title} you must master practical techniques. Theory is good, but techniques change lives. Let me list the key techniques for this course, and I will explain how to use each one.
""")
    for i, t in enumerate(techniques, 1):
        p.append(f"""
Technique {i}: {t}
{TECHNIQUE_STYLES[i % len(TECHNIQUE_STYLES)]}""")

    p.append(f"""
PART FIVE: SUMMARY AND ENCOURAGEMENT
----------------------------------------------------------------

My dear students, let us summarise what we have learned in {code} - {title}.

{SUMMARY_CLOSERS[list(COURSES).index(course) % len(SUMMARY_CLOSERS)]}

Remember these five truths:
{TRUTHS[list(COURSES).index(course) % len(TRUTHS)]}

I encourage you, my dear students. Do not be discouraged when a family does not change quickly. Change takes time. Be patient. Be kind. Be prayerful. Your work matters: you are helping marriages, protecting children, and healing communities. God bless you as you continue.

Key Terms to Remember
----------------------------------------------------------------
""")
    for t in terms:
        definition = COURSE_TERM_OVERRIDES.get((code, t)) or GLOSSARY.get(t, "")
        if definition:
            p.append(f"- {t}: {definition}\n")
        else:
            p.append(f"- {t}\n")

    p.append(f"""
Self-Test Questions - Answer in Your Notebook
----------------------------------------------------------------

1. Explain {concepts[0][0]} in your own simple words. Give one real life example.
2. Describe one real life practical from this lecture. What steps did you take, and in what order?
3. In the case studies, which case was most difficult? Why? What would you do first?
4. List three techniques from this course. Explain how you would teach each one to a Nigerian family.
5. How will you respect culture and faith when you work with a family in your community?
6. Write a short dialogue between a therapist and a couple who argue about money. Use active listening and one repair attempt.
7. What are the ethical duties of a family therapist? Give two examples from this course.
8. How will you set a small, achievable goal for a family, and how will you measure it?

Assignment
----------------------------------------------------------------

Write a 1,500-word assignment on one of these topics:
A. How {concepts[1][0]} applies to families in Nigeria today. Use two real life examples.
B. A detailed plan for one real life practical from this lecture. Include steps, sample dialogue, and a home assignment.
C. A case study of a family in your community (change names for confidentiality). Analyse the system, the strengths, and the intervention you would use.

Closing Prayer and Blessing
----------------------------------------------------------------

My dear students, thank you for listening to this lecture on {title}. May God give you wisdom to help families, patience to listen, and love to heal. May your own marriages and families be strong. May you go out and bring peace to every home you touch.

Go and practise. Go and help. Go and make a difference.

God bless you. See you in the next lecture.

================================================================================
END OF LECTURE: {code} - {title}
Triune Biblical University Global Extension, USA
PhD in Marriage and Family Therapy
================================================================================
""")
    return "".join(p)


def main():
    total = 0
    for course in COURSES:
        code, title, folder = course[0], course[1], course[2]
        text = build(course)
        words = len(text.split())
        total += words
        fname = f"{code.replace('.', '')}_{title.replace(' ', '_').replace('/', '')}.txt"
        path = os.path.join(BASE, folder, fname)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{code} {title}: {words:,} words")
    print(f"\nBASE TOTAL: {total:,} words in {len(COURSES)} files")


if __name__ == "__main__":
    main()
