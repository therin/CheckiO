# -*- coding: utf-8 -*-
'''
Sophie has found a stash books and she wants to find information about the ancients who lived on the islands. Unfortunately, she does not have a text search module and needs some help. Let's write a program to help her search for keywords on the pages of a book.

You are given some plain text (without tags) and a string with keywords (or parts of words, or letters) separated by spaces. You will need to find all the keywords and put these words into "<span></span>" wrappers to highlight them for Sophie. You can ignore upper or lower cases for the key words, but the original letter cases in the text should remain.

For the cases when keywords contain or intersect each other you should highlight the larger word without nested span tags. Let's look it with example.
The text "Hello World! Or LOL" and keywords "hell world or lo".
The word "World" contains two keywords thus we tag only larger part "<span>World</span>".
"Hello" contains two intersected words "hell" and "lo" and we tag the larger part again "<span>Hello</span>".
Be careful, a result like "<span>Hel<span>lo</span></span>" is considered wrong because it contains nested tags.

Input: Two arguments. A text and key words as strings.

Output: The text with wrapped key words.

checkio("This is only a text example for task example.", "example") ==
        "This is only a text <span>example</span> for task <span>example</span>."
 
checkio("Python is a widely used high-level programming language.", "pyThoN") ==
        "<span>Python</span> is a widely used high-level programming language.")
 
checkio("It is experiment for control groups with similar distributions.", "is im") ==
        "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions.")
 
checkio("The National Aeronautics and Space Administration (NASA).", "nasa  THE") ==
        "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>).")
 
checkio("Did you find anything?", "word space tree") ==
        "Did you find anything?")
checkio("Hello World! Or LOL", "hell world or lo") ==
        "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
How it is used: You see this task every day when use your browser or work with documents. Every time when you search something on the page and want to see the found fragments as highlighted parts, you encounter the concept seen in this task. This problem can be more complex if you use it for the languages where you need to write "lowercase" rules.

Precondition: 
0 < |text| < 5000
0 < |the number of key words| < 30
'''

def checkio(text, words):
    return text

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u"This is only a text example for task example.", u"example") ==
            "This is only a text <span>example</span> for task <span>example</span>."), "Simple test"

    assert (checkio(u"Python is a widely used high-level programming language.", u"pyThoN") ==
            "<span>Python</span> is a widely used high-level programming language."), "Ignore letters cases, but keep original"

    assert (checkio(u"It is experiment for control groups with similar distributions.", u"is im") ==
            "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."), "Several subwords"

    assert (checkio(u"The National Aeronautics and Space Administration (NASA).", u"nasa  THE") ==
            "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."), "two spaces"
    
    assert (checkio(u"Did you find anything?", "word space tree") ==
            "Did you find anything?"), "No comments"

    assert (checkio(u"Hello World! Or LOL", u"hell world or lo") ==
            "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"), "Contain or intersect"

