from fabric.api import env, cd, hosts, run

personal_site_dir = "/var/www/jeffnuss.com"
env.use_ssh_config = True


@hosts('digitalocean')
def deploy():
    """Deploy the code to my digitalocean server"""
    with cd(personal_site_dir):
        run('git pull')
