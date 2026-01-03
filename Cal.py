import tkinter as tk
from tkinter import ttk, messagebox
from typing import List


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("简易计算器")
        self.geometry("420x360")
        self._entries: List[tk.Entry] = []

        self._build_ui()

    def _build_ui(self):
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        lbl = ttk.Label(frm, text="输入数字（按需添加/删除），选择运算后点击计算：")
        lbl.pack(anchor=tk.W)

        self.entries_frame = ttk.Frame(frm)
        self.entries_frame.pack(fill=tk.X, pady=8)

        # start with two input fields
        self._add_entry()
        self._add_entry()

        btns_frame = ttk.Frame(frm)
        btns_frame.pack(fill=tk.X, pady=6)

        add_btn = ttk.Button(btns_frame, text="添加数字", command=self._add_entry)
        add_btn.pack(side=tk.LEFT)

        rem_btn = ttk.Button(btns_frame, text="删除最后一个", command=self._remove_entry)
        rem_btn.pack(side=tk.LEFT, padx=(6, 0))

        ops_frame = ttk.Frame(frm)
        ops_frame.pack(fill=tk.X, pady=6)

        ttk.Label(ops_frame, text="运算：").pack(side=tk.LEFT)
        self.op_var = tk.StringVar(value="+")
        op_menu = ttk.OptionMenu(ops_frame, self.op_var, "+", "+", "-", "*", "/")
        op_menu.pack(side=tk.LEFT, padx=(6, 0))

        calc_btn = ttk.Button(ops_frame, text="计算", command=self._calculate)
        calc_btn.pack(side=tk.LEFT, padx=(12, 0))

        clear_btn = ttk.Button(ops_frame, text="清空", command=self._clear_all)
        clear_btn.pack(side=tk.LEFT, padx=(6, 0))

        result_frame = ttk.Frame(frm)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=(12, 0))

        self.result_var = tk.StringVar(value="结果: ")
        result_lbl = ttk.Label(result_frame, textvariable=self.result_var, anchor=tk.CENTER)
        result_lbl.pack(fill=tk.BOTH, expand=True)

        # bind Enter key to calculate
        self.bind("<Return>", lambda e: self._calculate())

    def _add_entry(self):
        ent = ttk.Entry(self.entries_frame)
        ent.pack(fill=tk.X, pady=2)
        ent.insert(0, "0")
        self._entries.append(ent)

    def _remove_entry(self):
        if len(self._entries) <= 1:
            messagebox.showinfo("提示", "至少保留一个输入字段。")
            return
        ent = self._entries.pop()
        ent.destroy()

    def _gather_numbers(self) -> List[float]:
        nums: List[float] = []
        for ent in self._entries:
            text = ent.get().strip()
            if text == "":
                raise ValueError("发现空输入")
            # allow comma-separated numbers inside one field as convenience
            parts = [p.strip() for p in text.split(",") if p.strip()]
            for p in parts:
                try:
                    nums.append(float(p))
                except ValueError:
                    raise ValueError(f"无法解析为数字: {p}")
        return nums

    def _calculate(self):
        try:
            nums = self._gather_numbers()
            if len(nums) < 2:
                messagebox.showwarning("警告", "请提供至少两个数字进行运算。")
                return
            op = self.op_var.get()
            result = None
            if op == "+":
                result = sum(nums)
            elif op == "-":
                # left-associative subtraction
                it = iter(nums)
                result = next(it)
                for v in it:
                    result -= v
            elif op == "*":
                result = 1.0
                for v in nums:
                    result *= v
            elif op == "/":
                it = iter(nums)
                result = next(it)
                for v in it:
                    if v == 0:
                        raise ZeroDivisionError("除数为 0")
                    result /= v
            else:
                raise ValueError("未知运算")

            # format result nicely: integer if whole
            if result is not None:
                if abs(result - int(result)) < 1e-12:
                    display = str(int(result))
                else:
                    display = str(result)
                self.result_var.set(f"结果: {display}")

        except ZeroDivisionError as e:
            messagebox.showerror("错误", f"计算错误: {e}")
        except ValueError as e:
            messagebox.showerror("错误", f"输入错误: {e}")
        except Exception as e:
            messagebox.showerror("错误", f"未知错误: {e}")

    def _clear_all(self):
        for ent in self._entries:
            ent.delete(0, tk.END)
            ent.insert(0, "0")
        self.result_var.set("结果: ")


def main():
    app = CalculatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
