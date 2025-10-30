#!/usr/bin/env node
const { spawnSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

function ensureVenv(venvDir) {
  if (fs.existsSync(path.join(venvDir, 'bin', 'python')) || fs.existsSync(path.join(venvDir, 'Scripts', 'python.exe'))) {
    return;
  }
  const py = process.env.PYTHON || 'python3';
  const mk = spawnSync(py, ['-m', 'venv', venvDir], { stdio: 'inherit' });
  if (mk.status !== 0) {
    console.error('Failed to create virtual environment. Ensure Python 3 is installed.');
    process.exit(mk.status || 1);
  }
}

function pipInstall(venvDir, args) {
  const pipPath = process.platform === 'win32' ? path.join(venvDir, 'Scripts', 'pip') : path.join(venvDir, 'bin', 'pip');
  const res = spawnSync(pipPath, args, { stdio: 'inherit' });
  if (res.status !== 0) {
    process.exit(res.status || 1);
  }
}

function runPlaywrightInstall(venvDir) {
  const pyPath = process.platform === 'win32' ? path.join(venvDir, 'Scripts', 'python') : path.join(venvDir, 'bin', 'python');
  const res = spawnSync(pyPath, ['-m', 'playwright', 'install', 'chromium'], { stdio: 'inherit' });
  if (res.status !== 0) {
    process.exit(res.status || 1);
  }
}

(function main() {
  const repoRoot = path.join(__dirname, '..');
  const venvDir = path.join(repoRoot, '.npx-venv');
  const serverPy = path.join(repoRoot, 'server.py');

  ensureVenv(venvDir);

  // Install Python dependencies
  const requirements = path.join(repoRoot, 'requirements.txt');
  if (fs.existsSync(requirements)) {
    pipInstall(venvDir, ['install', '-r', requirements]);
  } else {
    // Fallback to pyproject dependencies (best effort)
    pipInstall(venvDir, ['install', '.']);
  }

  // Ensure Playwright browser is installed
  runPlaywrightInstall(venvDir);

  // Launch server
  const pyPath = process.platform === 'win32' ? path.join(venvDir, 'Scripts', 'python') : path.join(venvDir, 'bin', 'python');
  const child = spawn(pyPath, [serverPy], { stdio: 'inherit' });
  child.on('exit', (code) => process.exit(code == null ? 0 : code));
})();