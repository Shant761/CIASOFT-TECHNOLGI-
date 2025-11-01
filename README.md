# CIA SOFT Single-Page Site

This repository contains a standalone `index.html` file that renders the CIA SOFT landing page together with a small `validate_html.py` helper script for structure checks.

## Updating the Splash Logo

1. Prepare your logo as a square PNG or SVG (512×512 recommended). If you only have another format, convert it to PNG first so you can encode it easily.
2. Encode the file to Base64. For example, run `base64 -w0 your-logo.png > logo.b64` on Linux/macOS or use any online Base64 encoder.
3. Open `index.html` and search for `class="logo"`. Replace the long `src="data:image/..."` value with `data:image/png;base64,<your-encoded-string>` (or `image/svg+xml` if you encoded an SVG).
4. Keep the rest of the `<img>` tag (the `class` and `alt` attributes) unchanged so styling and accessibility continue to work.
5. Save the file and open it in a browser to verify the new emblem displays correctly.

Run `python validate_html.py` after edits to make sure the markup is still balanced.

## Validating the HTML

```
python validate_html.py
```

The script will report `HTML structure looks good!` if all tags are balanced. This gives a quick sanity check after manual edits.
