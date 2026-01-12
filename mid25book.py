{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMHhBgRitE5Fj+WSvcpmD9e",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bookkynakab/25-Book-coding68/blob/main/mid25book.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "currency = input(\"ระบุสกุลเงิน (USD หรือ JPY): \")\n",
        "amount = float(input(\"ระบุจำนวนเงิน: \"))\n",
        "\n",
        "if currency == 'USD':\n",
        "    thb = amount * 32.57\n",
        "    print(\"จำนวนเงินในหน่วยบาทคือ\", thb)\n",
        "elif currency == 'JPY':\n",
        "    thb = amount * 0.29\n",
        "    print(\"จำนวนเงินในหน่วยบาทคือ\", thb\n",
        "          )\n",
        "else:\n",
        "    print(\"ข้อมูลไม่ถูกต้อง กรุณาระบุเฉพาะ USD หรือ JPY\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uc-wIR77O1OX",
        "outputId": "92695eb7-d33b-48a5-bfbe-dbce557cff19"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ระบุสกุลเงิน (USD หรือ JPY): JPY\n",
            "ระบุจำนวนเงิน: 30.25\n",
            "จำนวนเงินในหน่วยบาทคือ 8.772499999999999\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "WdlHsWDLSkzZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}