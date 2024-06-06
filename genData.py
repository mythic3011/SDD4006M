import csv
import faker
import random
import threading

fake = faker.Faker("zh_CN")


def worker(thread_id, data):
    for _ in range(100):
        data.append(generate_data())
    print(f"Thread {thread_id} finished")


def generate_data():
    name = fake.name()
    age = random.randint(1, 5)
    gender = random.choice(["M", "F"])
    education = random.choice(
        ["none", "kindergarden", "Primary", "Secondary", "Undergradate", "Master / PHD"]
    )
    accessible = random.randint(1, 5)
    attracter = fake.name()
    understand_easy = random.randint(1, 10)
    find_easy = random.randint(1, 5)
    trust = random.randint(1, 5)
    useful = random.choice(
        [
            "REASONS OF THE DIVIDE",
            "Situation In Hong Kong",
            "The Impact on Education",
            "Widening Gaps",
            "Trust and Security Concerns",
            "Bridging the Gap",
        ]
    )

    valuable = random.choice(["Yes", "No", "Maybe"])
    challenges = random.choice(["Yes", "No", "Maybe"])
    much = random.choice(["Yes", "No", "Maybe"])
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "education": education,
        "accessible": accessible,
        "attracter": attracter,
        "understand_easy": understand_easy,
        "find_easy": find_easy,
        "trust": trust,
        "useful": useful,
        "challenges": challenges,
        "much": much,
        "valuable": valuable,
    }


def write_to_csv(data, filename):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    data = []
    threads = []

    for i in range(4):  # Create 4 threads
        t = threading.Thread(target=worker, args=(i, data))
        threads.append(t)
        t.start()

    for t in threads:  # Wait for all threads to finish
        t.join()

    write_to_csv(data, "output.csv")


if __name__ == "__main__":
    main()
