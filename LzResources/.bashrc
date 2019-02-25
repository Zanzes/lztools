# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -hltrF'
alias lla='ls -haltrF'
alias la='ls -ACF'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂

# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Alias START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

#alias reboot='systemctl reboot'
#alias poweroff='sudo poweroff'
alias cp='cp -rv'
alias mv='mv -v'
alias rm='rm -v'
alias cc='clear'
alias echo='echo -e'
#alias ll='ls -AlhF'
alias ee='exit'
alias poweroff='systemctl poweroff'
alias reboot='systemctl reboot'
alias suspend='systemctl suspend'
alias hibernate='systemctl hibernate'
alias hybrid-sleep='systemctl hybrid-sleep'
alias gg1="git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"
alias gg2="git log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all"
alias gg3="git log --all --decorate --oneline --graph"
alias docker="sudo docker"
alias python3='python3.7'
alias python='python3.7'
#alias dd='dd bs status=progress conv=fsync'
alias gdb='gdb -x ~/lab/gdb_cmd'

# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Alias END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Vars START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

branch='$(lgit branch -b 2>/dev/null)'

# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Vars END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Export START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

export mserv=$ip
export MediaServer=$ip
export BROWSER=lynx
export PS1="\[$(tput setaf 7)\]$branch\[$(tput bold)\]\[$(tput setaf 1)\]\u@\h \[$(tput setaf 2)\]\d \[$(tput setaf 4)\]\A \[$(tput setaf 6)\]\# \[$(tput setaf 5)\]\!  \[$(tput setaf 3)\]\w\[$(tput setaf 7)\]\n\\$> \[$(tput sgr0)\]"

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/dev
# export VIRTUALENVWRAPPER_SCRIPT=/home/zanzes/.virtualenvs/lztools/bin/virtualenvwrapper.sh
# source /home/zanzes/.virtualenvs/lztools/bin/virtualenvwrapper_lazy.sh 2> /dev/null
# source /usr/share/virtualenvwrapper/virtualenvwrapper_lazy.sh
# source /home/zanzes/.local/bin/virtualenvwrapper.sh
source /home/zanzes/.local/bin/virtualenvwrapper.sh


# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Export END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Other START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙

#shopt -s extdebug
#function auto_source_names {
#    local CMD="$BASH_COMMAND"
#    if [[ "$CMD" == dev-init* ]];then
#        #w=$(lwhere dev-init)
#        echo "Autosourcing"
#        eval ". $CMD"
#    elif [[ "$CMD" == pedit || "$CMD" == *"/pedit" ]];then
#        echo "Autosourcing"
#        eval ". $CMD"
#    fi
#}
#trap 'auto_source_names' DEBUG

# workon lztools
eval "$(_LZTOOLS_COMPLETE=source lztools 2> /dev/null)" 2> /dev/null
stty -ixon
PROMPT_COMMAND='source /home/zanzes/.lztools/scripts/data_loader 2> /dev/null'
#clear

# added by Anaconda3 installer
# export PATH="/home/zanzes/.anaconda3/bin:$PATH"

venv="work"

if [[ -n "$TMUX" ]]; then
    x=$(tmux list-panes | wc -l)
    if [[ $x == 1 ]];then 
        workon $venv
        tmux splitw -h
    elif [[ $x == 2 ]];then
        workon $venv
        tmux splitw
    elif [[ $x == 3 ]];then
        workon $venv
        htop
    fi
fi 

shopt -s extdebug
function auto_source_names {
    local CMD="$BASH_COMMAND"
    if [[ $CMD == *" -h" ]];then
        echo "Used auto --help"
        ${CMD/ -h/ --help}
        return 555
    fi
}
trap 'auto_source_names' DEBUG

export http_proxy=''
export https_proxy=''
export ftp_proxy=''
export socks_proxy=''

function iso-to-disk()
{
    if [[ $# != 2 ]]; then
        echo "Usage: dd {ISO} {DISK}"
        echo ""
        echo "Example:"
        echo "  If the iso is named example.iso and"
        echo "  the disk is named sdf"
        echo "  then the correct command would be:"
        echo ""
        echo "      dd example.iso /dev/sdf"
        echo ""
        echo "  Which would generate the complete command:"
        echo ""
        echo "      dd bs=4M if=example.iso of=/dev/sdf status=progress conv=fsync";
        echo ""
        (>&2 echo "Error: Missing argument")
    else
        sudo dd bs=4M if=$1 of=$2 status=progress conv=fsync
    fi
}
# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> Other END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙




