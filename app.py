from repositories import scrape_repositories
from developers import scrape_developers

trending_repositories = scrape_repositories()
trending_developers = scrape_developers()

print(trending_repositories)
print(trending_developers)