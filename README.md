# The ThingsDB Documentation source

### Prerequisites

You're going to need:

 - **Linux or macOS** — Windows may work, but is unsupported.
 - **Ruby, version 2.3.1 or newer**
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Getting Set Up

1. Fork this repository on GitHub.
2. Clone *your forked repository* (not our original one) to your hard drive with `git clone https://github.com/YOURUSERNAME/ThingsDocs.git`
3. `cd ThingsDocs`
4. Initialize and start Slate. You can either do this locally, or with Vagrant:

```shell
# either run this to run locally
bundle install
bundle exec middleman server

# OR run this to run with vagrant
vagrant up

# This is what I needed to do on Ubuntu 18.04
sudo apt-get install ruby-full build-essential patch ruby-dev zlib1g-dev liblzma-dev
sudo gem install fast_blank -v '1.0.0' --source 'https://rubygems.org/'
sudo gem install nokogiri -v '1.8.2' --source 'https://rubygems.org/'
bundle install
bundle exec middleman server

# Use docker
docker-compose up

```


You can now see the docs at http://localhost:4567. Whoa! That was fast!
