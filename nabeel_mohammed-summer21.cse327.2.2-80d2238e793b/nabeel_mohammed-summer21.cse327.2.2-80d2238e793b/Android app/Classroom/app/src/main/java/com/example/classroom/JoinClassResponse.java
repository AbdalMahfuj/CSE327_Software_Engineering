package com.example.classroom;

import java.io.Serializable;

public class JoinClassResponse implements Serializable {
    private String msg;

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
}