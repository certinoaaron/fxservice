#!/bin/bash
FLASK_APP="app/app.py" D_SERVICE="recharge-input" DD_AGENT_HOST=DDTRACE_HOST DD_TRACE_AGENT_PORT="8126" DD_LOGS_INJECTION=true ddtrace-run  flask run --host=0.0.0.0 --port=6101