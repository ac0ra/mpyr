if [[ ! -o interactive ]]; then
    return
fi

compctl -K _mpy mpy

_mpy() {
  local word words completions
  read -cA words
  word="${words[2]}"

  if [ "${#words}" -eq 2 ]; then
    completions="$(mpy commands)"
  else
    completions="$(mpy completions "${word}")"
  fi

  reply=("${(ps:\n:)completions}")
}