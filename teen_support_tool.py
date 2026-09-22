```python
def teen_support_tool():
    print("====================================")
    print("      AI TEEN SUPPORT TOOL")
    print("====================================")
    print()
    print("What area would you like guidance on?")
    print("1. Academic challenges")
    print("2. Friendships and peer pressure")
    print("3. Social media")
    print("4. Goals and personal development")
    print("5. Time management")

    choice = input("\nEnter a number (1-5): ")

    guidance = {
        "1": (
            "Academic challenges",
            "Start by identifying the specific subject or task you are struggling with. "
            "Break it into smaller tasks, create a realistic study schedule, and ask a "
            "teacher or trusted adult for help when needed."
        ),
        "2": (
            "Friendships and peer pressure",
            "Think about whether the situation aligns with your values and boundaries. "
            "You do not have to make a decision simply because your friends are doing "
            "something. Consider speaking with a trusted adult."
        ),
        "3": (
            "Social media",
            "Pay attention to how social media affects your time, emotions, and self-image. "
            "Consider setting healthy screen-time boundaries and taking regular breaks."
        ),
        "4": (
            "Goals and personal development",
            "Choose one clear goal and break it into smaller actions. Track your progress "
            "and review what is working each week."
        ),
        "5": (
            "Time management",
            "Write down your important tasks, identify your priorities, and allocate time "
            "for school, responsibilities, rest, and personal activities."
        )
    }

    if choice in guidance:
        topic, advice = guidance[choice]
        print(f"\nTopic: {topic}")
        print(f"Guidance: {advice}")
    else:
        print("\nPlease choose a number between 1 and 5.")

    print("\nRemember: this tool provides general educational guidance.")
    print("For serious or sensitive situations, speak with a trusted adult or qualified professional.")


if __name__ == "__main__":
    teen_support_tool()
```

Then scroll down and click **Commit changes**.

### What you've just done

You've created your first **Python program**.

It isn't using generative AI yet. That's intentional. We're building the project progressively:

**Version 1**
→ Python decision-based support tool

**Version 2**
→ Improve the user interaction

**Version 3**
→ Add an actual AI component

**Version 4**
→ Create a simple web interface

That gives you a much better story for your application: **you learned → built → tested → improved.**

Once you've committed `teen_support_tool.py`, tell me **done**. Then I'll show you how to actually **run it and test it**, even if you've never used Python before.
