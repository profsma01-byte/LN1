# -*- coding: utf-8 -*-
"""Additional varied blocks: technique teaching variants and extra practical labs."""

from narration_variants3 import LAB_CLOSERS

# Five different ways to teach a technique
TECHNIQUE_STYLES = [
"""
How to use it: begin with a plain invitation. "This is a way to help you talk better. Let us try it together." Then demonstrate it yourself, with a colleague or with your own words. Let the family practise while you watch, and give kind, specific feedback. Send the skill home as a small assignment. A technique works only when it is practised at home.

Real life tip: many Nigerian families respect proverbs. Teach this technique with a short proverb so it is remembered long after the session.

Common mistake: do not stack techniques. One per session, mastered, is worth more than five half-learned.
""",
"""
How to use it: first explain why the technique exists, not only what it is. Families cooperate when they understand the purpose. Second, model it in a low-stakes example, such as how to greet a neighbour. Third, have the family rehearse the real situation while you coach gently. Fourth, ask, "What felt natural, and what felt strange?" Fifth, agree on a practice plan for the week.

Real life tip: use the family's own names and situations in the rehearsal. Practice that sounds like their real life transfers to their real life.

Common mistake: correcting too much too soon. Let the first attempt be imperfect. Confidence comes before polish.
""",
"""
How to use it: teach it in three sentences. One, what it is. Two, when to use it. Three, what to say. Then show it. Then have the family show you. Then ask each member to name one moment this week when they will use it. Write those moments down and review them next session.

Real life tip: ask a respected elder or pastor to endorse the technique publicly. Cultural endorsement speeds adoption dramatically.

Common mistake: using the technique only in the office. If it stays in the office, nothing changes at home.
""",
"""
How to use it: start with a story. Tell a short story of a family who used the technique and what changed. Stories lower resistance and create hope. Then walk through the steps on paper so the family can see them. Then practise in pairs inside the room, with one person as the coach. End by asking, "What would make this hard at home, and how will you handle that?"

Real life tip: keep a small collection of true, anonymised stories from your practice and community. Stories travel further than instructions.

Common mistake: ignoring the obstacles the family names. If they say "my husband will not participate", that is the real problem to solve before the technique can work.
""",
"""
How to use it: use the teach-back method. Explain the technique briefly, then ask the family to teach it back to you in their own words. If they cannot, the teaching was not clear enough. Then rehearse it once, and once more with a small obstacle added, such as someone interrupting. Finish with a written note in simple language that they can keep at home.

Real life tip: write the note in the language the family thinks in, or provide a short voice note if literacy is limited. Accessibility is respect.

Common mistake: assuming understanding because heads were nodding. Nodding is politeness; teach-back is proof.
""",
]

# Extra practical labs, cycled so each course has more hands-on practice
EXTRA_LABS = [
    ("The Reflect-and-Plan Lab",
     "Take the first concept of this course, {c1}, and design a forty-minute session around it. Write your opening sentence, three questions, one demonstration, and one home task. Then run the session with classmates acting as the family. Record the feedback you receive: What landed? What confused them? What would you change? Bring your revised plan to supervision."),
    ("The Family Meeting Lab",
     "Convene a simulated family meeting on the topic of {c2}. Assign roles: a father who is sceptical, a mother who is exhausted, a teenager who is silent, and a grandmother who is powerful. Your task is to chair the meeting so that every voice is heard. Practise naming the rules, inviting the quiet member, and closing with appreciation. Debrief on the power dynamics you noticed."),
    ("The Boundary Lab",
     "Using the concept of {c3}, practise setting one boundary in three different tones: harsh, passive, and warm-but-firm. Say the same boundary three times and ask your partner which one they would actually obey and why. Then practise receiving pushback without escalating. Boundaries are a skill of the voice as much as of the mind."),
    ("The Culture Lab",
     "Take {c4} and adapt it for three different Nigerian family contexts: a rural Christian home, an urban Muslim home, and a diaspora family that has returned. For each, write how you would introduce the idea, which words you would avoid, and who you would ask for endorsement. Compare the three versions with your study group."),
    ("The Documentation Lab",
     "Write a clinical note for a session on {c5}. Include the presenting issue, the interaction you observed, your hypothesis, the intervention used, the family's response, the plan, and any risk considerations. Keep it factual and free of speculation. Then have a peer audit it for clarity, bias, and legal safety. Good notes protect families and therapists alike."),
]


def build_extra_labs(course_title, concepts):
    out = []
    for i, (lab_title, body) in enumerate(EXTRA_LABS):
        c1 = concepts[i % len(concepts)][0]
        c2 = concepts[(i + 3) % len(concepts)][0]
        c3 = concepts[(i + 6) % len(concepts)][0]
        c4 = concepts[(i + 9) % len(concepts)][0]
        c5 = concepts[(i + 11) % len(concepts)][0]
        text = body.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
        out.append(f"""
PRACTICAL LAB {i+1}: {lab_title}
----------------------------------------------------------------

{text}

{LAB_CLOSERS[i % len(LAB_CLOSERS)]}
""")
    return "".join(out)
