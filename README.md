# Dad Jokes

A small script for retrieving daily dad jokes from Twitter and using Github Actions and cron-job.org to send a message via MS Teams

# Create an MS Teams Webhook

1. Go to one of your teams channels and choose a channel
2. Next to the channel name, click on the triple dots
3. Click on "Connectors"
4. Next to "Incoming Webhook", click "Configure"
5. Choose a name
6. Scroll to the bottom and click "Create"
12. Copy the Webhook URL

# Store Wehbhook URL in Github Secrets

1. Navigate to this repo
2. Settings (for this repo)
3. Secrets
4. New repository secret
5. Set the name as "MS_TEAM_WEBHOOK"
6. Paste the copied Webhook URL as the value

# Store Twitter Bearer Token in Github Secrets

1. Navigate to this repo
2. Settings (for this repo)
3. Secrets
4. New repository secret
5. Set the name as "TWITTER_BEARER_TOKEN"
6. Paste the copied Twitter Bearer Token as the value

# Generate a Github Personal Access Token
1. Go to `https://github.com/settings/profile`
2. Developer Settings
3. Personal access tokens
4. Generate new token
4. Copy personal access token

# Setting Up Cron Job

1. Go to `console.cron-job.org`
2. Cronjobs
3. CREATE CRONJOB
4. COMMON Tab
5. Choose a title
6. Use `https://api.github.com/repos/seanlaw/dad_jokes/dispatches` for the URL
7. Choose an execution schedule
8. ADVANCED Tab
9. Key=Accept
10. Value=application/vnd.github.v3+json
11. +ADD
12. Key=Authorization
13. Value=token {personal access token}
14. POST request method
15. {"event_type":"run_dad_jokes"} request body. The event type must match the `types` found in the `.github/workflows/schedule.yml` file.
