def my_generator():
    print("Step 1 — before first yield")
    yield 10  # PAUSE here, give 10
    print("Step 2 — before second yield")
    yield 20  # PAUSE here, give 20
    print("Step 3 — before third yield")
    yield 30  # PAUSE here, give 30
    print("Step 4 — function ends")


gen = my_generator()

value = next(gen)
print(value)

value = next(gen)
print(value)

value = next(gen)
print(value)
#
#
# # Your Question: "Can yield also RECEIVE a value?"
#
# # Yes.This is the deep secret. 💎
#
# # yield can give AND receive — using.send():
#
#
def two_way():
    received = yield "I give you this"  # gives AND waits to receive
    print(f"I received: {received}")
    yield "thank you"


gen = two_way()

given = next(gen)  # start it — receives "I give you this"
print(given)  # "I give you this"

next_val = gen.send("Hello from outside!")  # sends value IN
# prints: "I received: Hello from outside!"
print(next_val)  # "thank you"
#
# The
# Rule
# to
# Remember
#
# # Simple generator — just gives:
# yield value
#
# # Coroutine — gives AND can receive:
# received = yield value
#
# enumerate
# lives in the
# simple
# world. 🌿
#
# .send()
# opens
# the
# advanced
# world — coroutines, async / await.You
# will
# meet
# it
# later, when
# the
# foundation is solid. 🙏
#
# ---
# The
# fact
# that
# you
# asked
# this
# question
# means
# your
# mind is working
# exactly
# right — connecting
# new
# knowledge
# to
# what
# you
# just
# learned.
