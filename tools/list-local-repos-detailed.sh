#!/usr/bin/env bash
set -euo pipefail
BASES=("$HOME" "/storage/shared" "$HOME/storage/shared")
OUT="$HOME/local-repos-detailed.json"
echo "[" > "$OUT"
first=true
escape() { printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/$/ /' | sed 's/ $//'; }
for BASE in "${BASES[@]}"; do
 [ -d "$BASE" ] || continue
  find "$BASE" -type d -name .git 2>/dev/null | while read -r gitdir; do
 repo=$(dirname "$gitdir")
 remote=$(git -C "$repo" remote get-url origin 2>/dev/null || git -C "$repo" remote -v 2>/dev/null | awk 'NR==1{print $2}' || echo "")
 branch=$(git -C "$repo" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")
 last_commit_sha=$(git -C "$repo" rev-parse --verify HEAD 2>/dev/null || echo "")
 last_commit_date=$(git -C "$repo" log -1 --format=%ci 2>/dev/null || echo "")
 last_commit_msg=$(git -C "$repo" log -1 --format=%s 2>/dev/null || echo "")
 uncommitted_count=$(git -C "$repo" status --porcelain 2>/dev/null | wc -l)
 uncommitted_changes=false
 [ "$uncommitted_count" -gt 0 ] && uncommitted_changes=true
    ahead=0; behind=0
    if git -C "$repo" rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
 counts=$(git -C "$repo" rev-list --left-right --count HEAD...@{u} 2>/dev/null || echo "0 0")
 ahead=$(echo $counts | awk '{print $1}')
      behind=$(echo $counts | awk '{print $2}')
 fi
 size_kb=$(du -sk "$repo" 2>/dev/null | awk '{print $1}' || echo 0)
    gh_owner=""; gh_repo=""
    if echo "$remote" | grep -qi "github.com"; then
 tmp=$(echo "$remote" | sed -E 's#^(git@|ssh://git@)github.com:##; s#^(https?://[^/]+/|git://[^/]+/)##; s/\.git$//')
      tmp=$(echo "$tmp" | sed 's#.*github.com[:/]\?\(.*\)$#\1#')
 gh_owner=$(echo "$tmp" | cut -d'/' -f1)
 gh_repo=$(echo "$tmp" | cut -d'/' -f2-)
 fi
 ppath=$(escape "$repo")
 premote=$(escape "$remote")
 pbranch=$(escape "$branch")
 plcsha=$(escape "$last_commit_sha")
 plcdate=$(escape "$last_commit_date")
 plcmsg=$(escape "$last_commit_msg")
 pgh_owner=$(escape "$gh_owner")
 pgh_repo=$(escape "$gh_repo")
 if [ "$first" = true ]; then first=false; else echo "," >> "$OUT"; fi
 printf '{' >> "$OUT"
    printf '"path":"%s",' "$ppath" >> "$OUT"
    printf '"remote":"%s",' "$premote" >> "$OUT"
    printf '"is_github":%s,' "$( [ -n "$gh_owner" ] && echo true || echo false )" >> "$OUT"
 printf '"github_owner":"%s",' "$pgh_owner" >> "$OUT"
 printf '"github_repo":"%s",' "$pgh_repo" >> "$OUT"
 printf '"branch":"%s",' "$pbranch" >> "$OUT"
 printf '"last_commit_sha":"%s",' "$plcsha" >> "$OUT"
 printf '"last_commit_date":"%s",' "$plcdate" >> "$OUT"
 printf '"last_commit_msg":"%s",' "$plcmsg" >> "$OUT"
 printf '"uncommitted_changes":%s,' "$uncommitted_changes" >> "$OUT"
 printf '"ahead":%s,' "$ahead" >> "$OUT"
 printf '"behind":%s,' "$behind" >> "$OUT"
 printf '"size_kb":%s' "$size_kb" >> "$OUT"
 printf '}' >> "$OUT"
  done
done
echo "]" >> "$OUT"
echo "Wrote $OUT"
