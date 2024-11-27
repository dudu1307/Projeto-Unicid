import tkinter as tk
from tkinter import messagebox, simpledialog

class ListaDeTarefas:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")
        
        self.tarefas = []
        
        self.lista = tk.Listbox(master, selectmode=tk.SINGLE, width=50, height=10)
        self.lista.pack(pady=20)
        
        self.adicionar_button = tk.Button(master, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.adicionar_button.pack(pady=5)
        
        self.editar_button = tk.Button(master, text="Editar Tarefa", command=self.editar_tarefa)
        self.editar_button.pack(pady=5)
        
        self.concluir_button = tk.Button(master, text="Concluir Tarefa", command=self.concluir_tarefa)
        self.concluir_button.pack(pady=5)
        
        self.excluir_button = tk.Button(master, text="Excluir Tarefa", command=self.excluir_tarefa)
        self.excluir_button.pack(pady=5)

    def adicionar_tarefa(self):
        tarefa = simpledialog.askstring("Nova Tarefa", "Digite a tarefa:")
        if tarefa:
            self.tarefas.append(tarefa)
            self.atualizar_lista()

    def editar_tarefa(self):
        try:
            selecionada = self.lista.curselection()[0]
            tarefa = simpledialog.askstring("Editar Tarefa", "Edite a tarefa:", initialvalue=self.tarefas[selecionada])
            if tarefa:
                self.tarefas[selecionada] = tarefa
                self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Editar Tarefa", "Selecione uma tarefa para editar.")

    def concluir_tarefa(self):
        try:
            selecionada = self.lista.curselection()[0]
            tarefa_concluida = self.tarefas[selecionada] + " (concluída)"
            self.tarefas[selecionada] = tarefa_concluida
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Concluir Tarefa", "Selecione uma tarefa para concluir.")

    def excluir_tarefa(self):
        try:
            selecionada = self.lista.curselection()[0]
            del self.tarefas[selecionada]
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Excluir Tarefa", "Selecione uma tarefa para excluir.")

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista.insert(tk.END, tarefa)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTarefas(root)
    root.mainloop()
