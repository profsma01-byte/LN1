# -*- coding: utf-8 -*-
"""Quality layer: coherent bridges, distinct dialogues, varied closings."""

# 13 bridges that read naturally for ANY concept title (no forced metaphors)
BRIDGE_A = [
"Let me say this as simply as I can. {t} is not a label you paste on a person. It is a way of seeing how people move together, the way you would watch dancers and notice who leads, who follows, and who keeps stepping on whose toes. Once you can see the dance, you can teach a new step.",
"Now let me explain it plainly, the way I would explain it to a market woman in Ibadan. {t} simply means that people in a family carry each other. If one person carries too much, the others feel lighter but weaker. If one person lets go, everyone stumbles. Balance is the goal, not perfection.",
"Here is the simple English version. {t} means that behaviour in a family is not random. It follows a pattern, and patterns can be learned and unlearned. Nobody teaches a family to quarrel every Sunday, yet the quarrel appears like a visitor who knows the time. Therapy teaches the family to change the appointment.",
"In plain words, {t} is about who carries the weight and who carries the blame. In unhealthy families, the weakest person often carries both. In healthy families, the weight is shared and blame is replaced by responsibility. That shift is the heart of our work.",
"Let me use a market example. A trader in Bodija market knows the price of every item and the mood of every customer. That is systems awareness. {t} asks you to bring the same awareness into the family. Who is tense today? Who is quiet? What changed since last week? Read the family the way a trader reads a market.",
"Let me put it simply. In plain terms, {t} is the study of what happens between people, not just inside them. A man may be patient at work and impatient at home, and the difference is not in his character alone; it is in the patterns of the home. Change the pattern, and you often change the man.",
"Let me give you the short version. {t} says that every family is trying to solve a problem, even when the solution looks like the problem. The husband who stays late at the office may be avoiding a fight. The wife who shouts may be trying to be heard. Look for the purpose behind the behaviour before you judge it.",
"Here is another way of saying it. {t} is about the rules nobody wrote down. Every family has them: who speaks first, who decides money, who is allowed to be angry, who must always be strong. Once you can name those unwritten rules, the family can decide whether to keep them or rewrite them.",
"Let me explain it as a doctor would. A doctor does not treat a symptom without examining the body. {t} is the examination of the family body. The symptom is only the complaint at the door; the illness is in the circulation of love, respect, and truth between members. Treat the circulation, and the symptom often fades.",
"Now, why does {t} matter so much in our setting? Because in Nigeria, a family is rarely just two people. It is grandparents, uncles, aunties, in-laws, pastors, imams, and neighbours. Whatever we study in this course must be applied with that wider family in view. A therapy that ignores the extended family will be outvoted by it.",
"Let me be practical. When {t} is handled badly, the damage rarely stays with one person. It moves to the children, then to the children's children. When it is handled well, the benefit moves in exactly the same way. That is why your work in this course is not a small thing; it is generational work.",
"I want you to notice something important. What we are calling {t} here is not a theoretical idea you will admire and forget. It is a lens that changes what you see in the first ten minutes of a session. Two therapists can sit in the same room with the same family; the one who understands {t} will see a pattern, while the other will only see a problem.",
"Let me put it in the language of responsibility. To study {t} is to ask every member of the family, gently but firmly, one question: what is your part in this, and what will you do about it? Not the other person's part. Your part. That question has rebuilt more homes than any lecture.",
]

# 13 distinct clinical dialogues
DIALOGUES_13 = [
"""Therapist: "Thank you both for coming. Before we begin, let me say what I already see: two people who are still here, still trying. Who would like to start?"
Wife: "I am tired of being ignored."
Therapist: "Ignored. That is a strong word. Can you give me one recent moment when you felt ignored?"
Wife: "Last night. I spoke and he kept looking at his phone."
Therapist: "And when she spoke and you kept looking at the phone, what was happening for you?"
Husband: "I was reading work messages. I did not know she needed me."
Therapist: "So one of you needed attention and the other did not know it was being asked for. That gap is where we will work.\"""",

"""Therapist: "When the two of you argue about this, what do you hear in your mind?"
Husband: "I hear that I am a failure."
Therapist: "And what do you hear, madam?"
Wife: "I hear that I am not a good wife."
Therapist: "You see, you are not really fighting each other. You are fighting two old voices. Let us separate the voices from the people, and then we can talk about the actual problem.\"""",

"""Therapist: "Describe a normal Tuesday in your house."
Father: "We wake, we rush, we work, we come home, we sleep."
Therapist: "Where is the part of Tuesday when the family is actually together?"
Father: (silence)
Therapist: "That silence is important. It is telling us something. What would you like Tuesday to look like?"
Father: "I would like to eat with them."
Therapist: "Then let us build Tuesday around that meal.\"""",

"""Therapist: "Your mother called you lazy. What happened inside you when she said it?"
Teenager: "I stopped listening."
Therapist: "That is honest. And what would you have wanted her to say instead?"
Teenager: "That she is worried, not that I am useless."
Therapist: "That is a sentence we can work with. Mother, could you say what you actually feel, using his sentence as a guide?"
Mother: "I am worried about your future. I am afraid for you."
Teenager: "Then say that. I can hear that.\"""",

"""Therapist: "On a scale of one to ten, how safe does this home feel to each of you?"
Wife: "Four."
Husband: "Seven."
Therapist: "Two different numbers under one roof. That is worth understanding. Wife, what makes it a four?"
Wife: "I never know his mood when he comes in."
Therapist: "Husband, what would it take for her number to rise by one point this week?"
Husband: "I can call her before I leave work."
Therapist: "That is a real, doable step. Let us test it this week.\"""",

"""Therapist: "You said your son is stubborn. Tell me about a time this week when he was not stubborn."
Mother: (pause) "On Sunday, when we cooked together."
Therapist: "What was different about Sunday?"
Mother: "I was not rushing. I was just with him."
Therapist: "So connection changed his behaviour before discipline did. That is a very important discovery. What would it take to have two Sundays in a week?\"""",

"""Therapist: "Everyone in this family has been carrying something alone. Today I want us to put some of it down. Who will start?"
Grandmother: "I will. I am tired of being the one who keeps the peace."
Therapist: "Thank you for your courage. And when you keep the peace, who is freed from doing it?"
Grandmother: "Everyone else."
Therapist: "So your burden has become their permission to stay silent. Let us see if we can share that load differently.\"""",

"""Therapist: "I am going to ask a strange question. If the problem disappeared tonight, what is the first small thing you would notice tomorrow morning?"
Husband: "She would greet me at the door."
Wife: "He would ask about my day."
Therapist: "So the miracle is not a mansion or a lottery win. It is a greeting and a question. That tells me your marriage is closer to healing than you think.\"""",

"""Therapist: "You have both said the word respect many times. What does respect look like in your house, in actions, not in theory?"
Wife: "He would not correct me in front of his mother."
Husband: "She would not discuss our money with her sister."
Therapist: "Now we have something specific. These are not feelings; these are agreements. Let us write them down and test them for two weeks.\"""",

"""Therapist: "I notice you have not looked at your husband since you sat down."
Wife: "There is nothing to look at."
Therapist: "That sentence carries a lot of pain. I am not here to judge it. I am here to understand it. When did you stop looking at him?"
Wife: (crying) "When he stopped looking at me."
Therapist: "Then let us begin exactly there. One look, one sentence, one honest moment.\"""",

"""Therapist: "Your daughter says she feels unheard. What do you hear when she says that?"
Father: "I hear that I have failed as a father."
Therapist: "So her pain lands on your shame, and your shame responds with anger. Do you see the cycle?"
Father: "I do."
Therapist: "Good. Then the next time she speaks, try to hear her pain without hearing a verdict about you. That is the skill we will practise today.\"""",

"""Therapist: "Both of you have said you want the marriage to work. What has each of you done in the last month that made it a little better?"
Husband: "I stopped shouting."
Wife: "I stopped bringing my mother into our arguments."
Therapist: "So you are both already working. That means I am not starting from zero. I am joining a project that is already underway.\"""",

"""Therapist: "Let us talk about money, but not about who is right. When you were growing up, what did your family teach you about money?"
Husband: "That a man must provide, no matter what."
Wife: "That a woman must save, because men cannot be trusted with money."
Therapist: "Now I understand the fight. You are not arguing about naira. You are arguing about two childhoods. Let us negotiate between those childhoods.\"""",
]

# 5 varied case-module closings
CASE_CLOSERS = [
"Remember, every case teaches you something. Keep a case diary. Record what you did, what worked, and what you would do differently. Over time, that diary becomes your own clinical textbook.",
"Before you close your notebook, ask yourself one more question: what would this family need from me if they returned next week, and what would they need from their own community? Therapy is part of a larger web of care.",
"A case is never only a case. It is a family with a name, a history, and a future. Hold that weight gently, and let it keep you humble.",
"If you take nothing else from this case, take this: the family that appears broken is usually a family that has been trying, in the dark, with tools that do not fit. Your job is to turn on the light and hand them better tools.",
"Write down the one sentence you would say to this family if you had only one sentence to give. That sentence, spoken with warmth at the right moment, may do more than an entire treatment manual.",
]
