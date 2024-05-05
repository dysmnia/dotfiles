PROMPT=" %{$fg[black]%}%~%{$reset_color%}"
PROMPT+=' $(git_prompt_info)%(?:%{$fg_bold[magenta]%}󰣐 :%{$fg_bold[red]%}󰋔 )'

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}git:(%{$fg[magenta]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"
