#!/usr/bin/python3
"""Task 0: Simple string templating invitation generator."""

PLACEHOLDERS = ("name", "event_title", "event_date", "event_location")


def _value_or_na(attendee, key):
    """Return attendee value for key, or N/A when missing/None."""
    value = attendee.get(key, "N/A")
    if value is None:
        return "N/A"
    return str(value)


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee dictionaries."""
    if not isinstance(template, str):
        print(
            "Invalid input type: template must be a string, "
            f"got {type(template).__name__}."
        )
        return

    if not isinstance(attendees, list):
        print(
            "Invalid input type: attendees must be a list of dictionaries, "
            f"got {type(attendees).__name__}."
        )
        return

    invalid_attendee = next(
        (attendee for attendee in attendees if not isinstance(attendee, dict)),
        None
    )
    if invalid_attendee is not None:
        print(
            "Invalid input type: attendees must be a list of dictionaries, "
            f"found {type(invalid_attendee).__name__}."
        )
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        rendered = template
        for key in PLACEHOLDERS:
            rendered = rendered.replace(f"{{{key}}}", _value_or_na(attendee, key))

        output_file_name = f"output_{index}.txt"
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            output_file.write(rendered)
