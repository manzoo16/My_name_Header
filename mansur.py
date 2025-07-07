from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

# Gradient-style "MANSUR"
title = Text("MANSUR", justify="center")
title.stylize("bold blue", 0, 1)
title.stylize("bold cyan", 1, 2)
title.stylize("bold green", 2, 5)
title.stylize("bold yellow", 5, 6)

# Boot Script subtitle
subtitle = Text("Boot Script 2.0", style="bold grey74", justify="right")

# Combine text elements
panel_content = Text.assemble(title, "\n", subtitle)

# Print in a colored panel
console.print(Panel(panel_content, border_style="magenta", padding=(1, 4)))