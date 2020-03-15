if [[ ! -o interactive ]]; then
    return
fi

compctl -K _mpyr mpyr

_mpyr() {
  local word words completions
  read -cA words
  word="${words[2]}"

  if [ "${#words}" -eq 2 ]; then
    completions="$(mpyr commands)"
  else
    completions="$(mpyr completions "${word}")"
  fi

  reply=("${(ps:\n:)completions}")
}
