from playwright.async_api import async_playwright
import asyncio

async def scrape_topics():
    data = []

    try:
        async with async_playwright() as playwright:
            browser = await playwright.webkit.launch() 

            page = await browser.new_page()
            await page.goto("https://github.com/topics")
            # content = await page.content()
            # print(content)

            for i in range(2):
                # print("Loop ", i)
                await page.locator("xpath=//form/button").click()
                await asyncio.sleep(2)
            
            topics_list = await page.locator(".py-4.border-bottom.d-flex.flex-justify-between").all()

            for topic in topics_list:
                avatar_url = None
                
                check_avatar = await topic.locator('//a[1]/div').count()
                if check_avatar:
                    print("avatar not exists")
                else:
                    # print("avatar exists")
                    avatar_url = await topic.locator('//a[1]/img').get_attribute("src")
                    # print(avatar_url)

                url = await topic.locator('//a[2]').get_attribute("href")
                title = await topic.locator('//a[2]/p[1]').inner_text()
                description = await topic.locator('//a[2]/p[2]').inner_text()

                # print(url)
                # print(title)
                # print(description)

                data.append({
                    "avatar_url": avatar_url,
                    "url": url,
                    "title": title,
                    "description": description
                })

            await page.screenshot(path="screenshot.png", full_page=True)
            await browser.close()

            return data

    except Exception as e:
        print(f"An unexcepted error occured: {e}")
        return []
    
# data = asyncio.run(scrape_topics())

# print(data)