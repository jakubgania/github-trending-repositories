from repositories import scrape_repositories
from developers import scrape_developers

import datetime
import json
import os

def run():
    trending_repositories = scrape_repositories()
    trending_developers = scrape_developers()

    # print(trending_repositories)
    # print(trending_developers)

    save_dir = "/app"

    # with open("repositories.json", "w") as f:
    with open(os.path.join(save_dir, "repositories.json"), "w") as f:
        f.write(
            json.dumps(trending_repositories, indent=2)
        )


    # with open("developers.json", "w") as f:
    with open(os.path.join(save_dir, "developers.json"), "w") as f:
        f.write(
            json.dumps(trending_developers, indent=2)
        )

run()