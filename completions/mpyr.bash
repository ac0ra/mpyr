_mpyr() {
  COMPREPLY=()
  local word="${COMP_WORDS[COMP_CWORD]}"

  if [ "$COMP_CWORD" -eq 1 ]; then
    COMPREPLY=( $(compgen -W "$(mpyr commands)" -- "$word") )
  else
    local command="${COMP_WORDS[1]}"
    local completions="$(mpyr completions "$command")"
    COMPREPLY=( $(compgen -W "$completions" -- "$word") )
  fi
}

complete -F _mpyr mpyr
