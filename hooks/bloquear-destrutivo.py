#!/usr/bin/env python3
"""Nega git push --force, git reset --hard, rm -rf e DROP TABLE."""

import json
import re
import sys


def emit(payload: dict) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")


def destructive(command: str) -> bool:
    if re.search(r"\bgit\s+reset\s+--hard\b", command):
        return True
    if re.search(r"\bgit\s+push\b", command) and (
        re.search(r"(?:^|\s)--force(?:\s|$)", command)
        or re.search(r"(?:^|\s)-f(?:\s|$)", command)
    ):
        return True
    if re.search(r"\bDROP\s+TABLE\b", command, re.IGNORECASE):
        return True
    if re.search(r"\brm\b", command):
        flags = re.findall(r"(?:^|\s)(-[A-Za-z]+)", command)
        letters = "".join(flag[1:] for flag in flags)
        if "r" in letters and "f" in letters:
            return True
        if "--recursive" in command and "--force" in command:
            return True
    return False


def main() -> int:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        emit(
            {
                "permission": "deny",
                "user_message": "O hook não leu o comando. Ele foi bloqueado.",
                "agent_message": "beforeShellExecution recebeu JSON inválido e falhou fechado.",
            }
        )
        return 0

    command = data.get("command") or ""
    if not isinstance(command, str):
        command = str(command)

    if destructive(command):
        emit(
            {
                "permission": "deny",
                "user_message": "Comando destrutivo bloqueado pelo harness.",
                "agent_message": "O hook negou git push --force, git reset --hard, rm -rf ou DROP TABLE.",
            }
        )
        return 0

    emit({"permission": "allow"})
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        emit(
            {
                "permission": "deny",
                "user_message": "O hook de comando destrutivo falhou e bloqueou a execução.",
                "agent_message": f"bloquear-destrutivo.py: {exc}",
            }
        )
        raise SystemExit(0)
