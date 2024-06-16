import subprocess
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import git

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

repos = ["https://github.com/ElGiaf/WebsiteHackingWithPython",'https://github.com/danielWagn/hackingWithPython','https://github.com/jazurka/HmP']

with open("vulnerabilities.txt", "w") as f:

    for repository_url in repos:

        driver.get(repository_url)

        time.sleep(5)

        repo_dir = "clonedRepo"
        #if os.path.exists(repo_dir):
        #    subprocess.run(["rm", "-rf", repo_dir])
        git.Repo.clone_from(repository_url, repo_dir)

        result = subprocess.run(["bandit",'-c','bandit.yml', "-r", repo_dir], capture_output=True, text=True)


        f.write("Bandit Output:"+repository_url+"\n")
        f.write(result.stdout)
        f.write("\n")

        subprocess.run(["rmdir", "/S", "/Q", repo_dir], capture_output=True, text=True, shell=True)

driver.quit()
print ('done')