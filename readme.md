# Telegram File Store Bot

A simple Telegram bot that allows users to upload files securely, with options for password protection and file descriptions. The bot tracks usage statistics and provides premium plans for enhanced features.

## Pricing

- **Basic Plan**: 50 Rs - 5 GB storage
- **Standard Plan**: 100 Rs - 20 GB storage + Password protection
- **Premium Plan**: 250 Rs - 50 GB storage + All features included

## Features

- 📁 Upload files securely
- 🔒 Optional password protection
- 📝 Add descriptions for files (60-80 characters)
- 📊 Track upload statistics
- 🛠️ Commands for user management (ban users)
- 💎 Premium plans for advanced storage options

## Commands

- `/start` - Welcome message
- `/help` - List available commands
- `/stats` - Show upload statistics
- `/premium` - View premium plans
- `/ban @username duration` - Ban a user from uploading files (e.g., `/ban @xyz 2 days`)

## How the Bot Works

1. Users can upload files to the bot.
2. Upon upload, the bot prompts the user to add a password or description.
3. Users can check their upload statistics and view premium plans.
4. Admins can ban users from uploading files if necessary.

## Hosting the Bot

You can host this bot on various platforms. Here are some options:

### 1. Koyeb

**Step-by-Step Guide to Deploy on Koyeb:**

1. **Create a Koyeb Account**: Sign up at [Koyeb](https://koyeb.com/).
  
2. **Create a New Service**:
   - Go to your Koyeb dashboard.
   - Click on "Create Service."
   - Choose the "Deploy from GitHub" option.

3. **Connect Your GitHub**:
   - Authorize Koyeb to access your GitHub account.
   - Select the repository where the bot code is stored.

4. **Configure Your Service**:
   - Choose the "Docker" option for runtime.
   - Set the environment variable for your bot token and channel ID:
     ```
     TOKEN=your_bot_token
     CHANNEL_ID=@your_channel_id
     ```

5. **Deploy**: Click on "Create Service" to deploy your bot.

6. **Monitor Logs**: After deployment, you can monitor logs to check if the bot is running correctly.

### 2. Heroku

1. **Create a Heroku Account**: Sign up at [Heroku](https://www.heroku.com/).
2. **Install the Heroku CLI**: Follow the instructions on the Heroku website to install the CLI.
3. **Create a New App**: Use the Heroku dashboard or CLI to create a new app.
4. **Deploy Your Code**: Push your code to Heroku using Git.
5. **Set Environment Variables**: In the Heroku dashboard, go to "Settings" > "Config Vars" and add your `TOKEN` and `CHANNEL_ID`.
6. **Start the Dyno**: Ensure your dyno is running.

### 3. AWS Elastic Beanstalk

1. **Create an AWS Account**: Sign up at [AWS](https://aws.amazon.com/).
2. **Install AWS CLI**: Follow the instructions to install the AWS CLI.
3. **Create a New Elastic Beanstalk Application**: Use the AWS Management Console.
4. **Deploy Your Code**: Zip your application code and upload it.
5. **Set Environment Variables**: Go to the configuration and set your `TOKEN` and `CHANNEL_ID`.

## Conclusion

This Telegram bot is designed to be user-friendly and straightforward, making it easy for anyone to manage file uploads securely. By following the hosting guides above, you can have your bot running in no time. Enjoy your new bot, and feel free to customize it further!

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=fileprotectbot&type=git&repository=utkarshdubey2008%2Ffileprotectbot&branch=main&builder=buildpack&regions=was&env%5B%5D=&ports=8000%3Bhttp%3B%2F)
