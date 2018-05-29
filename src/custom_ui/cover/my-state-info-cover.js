StateInfo = customElements.get('state-info')

class MyStateInfoCover extends StateInfo {
  static get template() {
    return Polymer.html`
    <style>
      :host {
        @apply --paper-font-body1;
        min-width: 120px;
        white-space: nowrap;
      }

      state-badge {
        float: left;
      }

      .info {
        margin-left: 56px;
      }

      .name {
        @apply --paper-font-common-nowrap;
        color: var(--primary-text-color);
        line-height: 20px;
      }

      .name[in-dialog], :host([secondary-line]) .name {
        line-height: 20px;
      }

      .time-ago, .extra-info, .extra-info > * {
        @apply --paper-font-common-nowrap;
        color: var(--secondary-text-color);
      }
    </style>

    <state-badge state-obj="[[stateObj]]"></state-badge>

    <div class="info">
      <div class="name" in-dialog\$="[[inDialog]]">[[computeStateName(stateObj)]]</div>
      <div class="extra-info">Position: [[computeStatePosition(stateObj)]]</div>

      <!-- <template is="dom-if" if="[[inDialog]]">
        <div class="time-ago">
          <ha-relative-time datetime="[[stateObj.last_changed]]"></ha-relative-time>
        </div>
      </template> -->
      <template is="dom-if" if="[[!inDialog]]">
        <div class="extra-info">
          <slot>
        </slot></div>
      </template>
    </div>
    `
  }


  computeStatePosition(stateObj) {
    return stateObj.attributes.current_position;
  }
}

customElements.define('my-state-info-cover', MyStateInfoCover);
