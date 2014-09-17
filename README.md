# Minim

I want to make a scripting language, and I want to also improve my general
ability in programming. This project is going to (hopefully) allow me to both of
these things. I am going to slowly write an implementation of my own language,
whic may or may not turn out to be useful for people. The development will be
done in incremental parts.

Here's how each part will be documented:

### Part x: Descriptional Name

Description of implementation.

**Specification:** Specific details on the certain part of the language
implementation.

**Code:** Where to look in the source code for the main source for the certain
part.

--

### Part 1: Function Calls

I'm not sure whether or not this is an odd thing to implement first, but I'm
doing it anyway. I want functions to be called with a lisp style (although this
language is not going to be a lisp derivative), and I want to start out with
basic standard-library-esque functions.

**Specification:** Functions in Minim are called as `(name arg1 arg2 ar...)`.

**Code:** `minim.py:19`, `functions.py`, `library.py:27`
